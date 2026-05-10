from unittest.mock import patch

from django.test import TestCase, override_settings
from django.urls import reverse


class ContactViewTests(TestCase):
    def setUp(self):
        self.url = reverse("home_app:contact")

    def test_get_contact_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    @override_settings(
        BREVO_API_KEY="",
        CONTACT_EMAIL="inbox@test.com",
        DEFAULT_FROM_EMAIL="from@test.com",
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    )
    def test_post_valid_redirects_and_sends_mail(self):
        from django.core import mail

        mail.outbox.clear()
        response = self.client.post(
            self.url,
            {
                "nombre": "Nombre",
                "email": "user@example.com",
                "mensaje": "Cuerpo del mensaje.",
            },
        )
        self.assertRedirects(
            response,
            reverse("home_app:contact_success"),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Cuerpo del mensaje", mail.outbox[0].body)

    def test_post_without_message_returns_form_error(self):
        response = self.client.post(
            self.url,
            {
                "nombre": "Nombre",
                "email": "user@example.com",
                "mensaje": "",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("mensaje", response.context["form"].errors)

    @patch("applications.home.views.send_contact_email", return_value=True)
    def test_post_valid_does_not_fail_when_send_is_mocked(self, _mock_send):
        response = self.client.post(
            self.url,
            {
                "nombre": "A",
                "email": "a@example.com",
                "mensaje": "Hi",
            },
        )
        self.assertRedirects(
            response,
            reverse("home_app:contact_success"),
            status_code=302,
            target_status_code=200,
        )
