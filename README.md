# retegi.eus

Proyecto Django para [retegi.eus](https://retegi.eus).

## Desarrollo local con Docker (código en caliente, puerto 8090)

Desde el directorio del proyecto (donde está `manage.py`):

```bash
cp .env.example .env   # y edita valores mínimos (p. ej. DJANGO_SECRET_KEY)
docker compose build
docker compose up
```

La app queda en `http://127.0.0.1:8090` (según `docker-compose.override.yml`).

## Producción con Docker

1. En el servidor, copia `.env.example` → `.env` y configura secretos, `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS`, `DATABASE_URL` (p. ej. Postgres), claves Brevo, etc.
2. Crea directorios persistidos si no existen: `data/`, `media/`, `staticfiles/`.
3. Construye e inicia (Gunicorn en el puerto interno 8000; el host expone **8090**):

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml build
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

4. Migraciones y estáticos (tras el primer arranque o en cada despliegue):

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml exec web python manage.py migrate
docker compose -f docker-compose.yml -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

5. Comprobaciones:

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml exec web python manage.py check
docker compose -f docker-compose.yml -f docker-compose.prod.yml exec web python manage.py check --deploy
```

**Notas:** el `Dockerfile` usa Gunicorn (`retegi.wsgi:application`). En producción no se usa `runserver`. Los estáticos recogidos van a `staticfiles/` (volumen) y se sirven con WhiteNoise. Los archivos subidos por usuarios deben resolverse con Nginx u otro proxy sirviendo `MEDIA_ROOT` o una configuración equivalente.

Cada vez que cambies `requirements.txt`, vuelve a construir la imagen: `docker compose build web` (o `docker compose build`).

## Dependencias Python

El archivo `requirements.txt` lista solo **dependencias directas**; `pip` instala el resto (p. ej. `requests` vía django-allauth/rosetta, `slippers` y `django-widget-tweaks` vía `django-allauth-ui`, Twisted/autobahn vía `daphne`, etc.).

## Frontend / npm

Hay un `package.json` con dependencia opcional de TinyMCE; el admin y los formularios usan **django-tinymce** y en plantillas suele cargarse TinyMCE desde CDN. No hace falta `node_modules` en el repositorio: tras `npm install` local, `node_modules/` queda ignorado por `.gitignore`.

## Variables de entorno

Ver `.env.example`.
