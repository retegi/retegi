"""Envío del formulario de contacto vía API Brevo o, si no está configurado, Django mail."""

from __future__ import annotations

import html
import logging
from typing import Any

import httpx
from django.conf import settings
from django.core.mail import EmailMessage

logger = logging.getLogger(__name__)

BREVO_SMTP_URL = "https://api.brevo.com/v3/smtp/email"


def send_contact_email(name: str, email: str, message: str) -> bool:
    """
    Envía el contacto. Si BREVO_API_KEY está definida, usa la API de Brevo;
    si no, usa el backend de email de Django (p. ej. consola en local).

    No expone detalles técnicos; solo devuelve True/False.
    """
    name = (name or "").strip()
    email = (email or "").strip()
    message = (message or "").strip()
    if not name or not email or not message:
        logger.warning("send_contact_email: datos incompletos (omitido envío).")
        return False

    api_key = (getattr(settings, "BREVO_API_KEY", None) or "").strip()
    if api_key:
        return _send_via_brevo(name, email, message)
    return _send_via_django_mail(name, email, message)


def _send_via_brevo(name: str, email: str, message: str) -> bool:
    api_key = (getattr(settings, "BREVO_API_KEY", None) or "").strip()
    if not api_key:
        logger.error("Brevo: clave API vacía.")
        return False

    sender_email = (getattr(settings, "BREVO_SENDER_EMAIL", None) or "").strip()
    sender_name = (getattr(settings, "BREVO_SENDER_NAME", None) or "").strip() or "retegi.eus"
    to_email = (getattr(settings, "BREVO_TO_EMAIL", None) or "").strip() or (
        getattr(settings, "CONTACT_EMAIL", None) or ""
    ).strip()

    if not sender_email:
        logger.error("Brevo: falta BREVO_SENDER_EMAIL.")
        return False
    if not to_email:
        logger.error("Brevo: falta BREVO_TO_EMAIL (y CONTACT_EMAIL vacío).")
        return False

    safe_name = html.escape(name)
    safe_mail = html.escape(email)
    safe_msg = html.escape(message).replace("\n", "<br>\n")

    html_content = (
        "<h2>Nuevo mensaje desde retegi.eus</h2>"
        f"<p><strong>Nombre:</strong> {safe_name}<br>"
        f"<strong>Email:</strong> {safe_mail}</p>"
        f"<hr><p style='white-space:pre-wrap'>{safe_msg}</p>"
    )

    payload: dict[str, Any] = {
        "sender": {"name": sender_name, "email": sender_email},
        "to": [{"email": to_email}],
        "replyTo": {"email": email, "name": name[:200]},
        "subject": "Nuevo mensaje desde retegi.eus",
        "htmlContent": html_content,
    }

    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json",
    }

    try:
        response = httpx.post(
            BREVO_SMTP_URL,
            json=payload,
            headers=headers,
            timeout=20.0,
        )
    except httpx.RequestError:
        logger.exception("Brevo: error de red al contactar con la API.")
        return False

    if response.status_code >= 400:
        logger.error(
            "Brevo: respuesta HTTP %s: %s",
            response.status_code,
            (response.text or "")[:800],
        )
        return False

    return True


def _send_via_django_mail(name: str, email: str, message: str) -> bool:
    """Usa EMAIL_BACKEND (p. ej. consola en desarrollo o SMTP)."""
    to_email = (getattr(settings, "CONTACT_EMAIL", None) or "").strip()
    if not to_email:
        logger.warning(
            "Envío contacto sin Brevo: CONTACT_EMAIL vacío; no se puede enviar. "
            "Configura BREVO_* o CONTACT_EMAIL."
        )
        return False

    from_email = (getattr(settings, "DEFAULT_FROM_EMAIL", None) or "").strip()
    if not from_email:
        logger.error("DEFAULT_FROM_EMAIL vacío; no se puede enviar el correo.")
        return False

    body = (
        f"Nombre: {name}\n"
        f"Email: {email}\n\n"
        f"{message}"
    )
    try:
        msg = EmailMessage(
            subject="[retegi.eus] Nuevo mensaje de contacto",
            body=body,
            from_email=from_email,
            to=[to_email],
            reply_to=[email],
        )
        msg.send(fail_silently=False)
    except Exception:
        logger.exception("Fallo al enviar correo con Django (SMTP/consola).")
        return False
    return True
