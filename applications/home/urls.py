from os import name
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PruebaEmail 

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

    path('contact/',
         views.ContactView.as_view(),
         name='contact',
    ),
    path('about/',
         views.AboutView.as_view(),
         name='about',
    ),

    path('cookies_policy/',
         views.CookiesPolicyView.as_view(),
         name='cookies_policy',
    ),
    path('privacy_policy/',
         views.ProvacyPolicyView.as_view(),
         name='privacy_policy',
    ),
    path('legal_policies/',
         views.LegalPoliciesView.as_view(),
         name='legal_policies',
    ),
     path('mail/', PruebaEmail.as_view(), name='mail'),
     path('trigger-task/', views.trigger_task, name='trigger_task'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)