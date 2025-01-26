from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponseRedirect
from . import views

# Redirige desde la raíz ('/') al idioma predeterminado
urlpatterns = [
    path('', lambda request: HttpResponseRedirect(f'/{settings.LANGUAGE_CODE.split("-")[0]}/')),
    path('admin/', admin.site.urls),
    path('assistant/', include('applications.assistant.urls')),
    #openai

]
# Incluye las rutas de Rosetta si está en INSTALLED_APPS
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]

# Prefijos de idioma para todas las rutas definidas con i18n_patterns
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),  # Para cambiar idioma
    path('', include('applications.home.urls')),  # Ruta de la aplicación principal
     
    path('accounts/', include('allauth.urls')),
)

# Opcional: Manejo de archivos estáticos si estás en modo DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
