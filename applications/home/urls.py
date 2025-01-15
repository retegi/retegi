from os import name
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home_app'

urlpatterns = [
    path('',
        views.HomePageView.as_view(),
        name='home',
    ),
    path('article/<int:pk>/',
        views.ArticleDetailView.as_view(),
        name='article_detail',
    ),
    path('article_create/',
         views.ArticleCreateView.as_view(),
        name='article_create',
    ),
    path('article_update/<int:pk>/',
         views.ArticleUpdateView.as_view(),
        name='article_update',
    ),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)