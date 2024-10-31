from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)


class HomeView(TemplateView):
    template_name = "home/index.html"