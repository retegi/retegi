from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    FormView
)
from .models import Post, Technology, Comment, Hacked
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.utils.dateformat import format
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from django.http import HttpResponse
#celery
from django.http import JsonResponse
from .tasks import example_task

import os
import json
import random
from django.conf import settings
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.views.generic import ListView
from .models import Post, Technology, Hacked

class HomePageView(ListView):
    template_name = "home/index.html"
    model = Post
    context_object_name = 'entradas_blog'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Obtener posts y datos relacionados
        context["post_list"] = Post.objects.all().order_by('-date_time')
        context["technology_list"] = Technology.objects.all()
        context["hacked_victims"] = Hacked.objects.all()

        # Procesar publicaciones por mes
        posts_by_month = (
            Post.objects.annotate(month=TruncMonth('date_time'))  # Trunca la fecha por mes
            .values('month')  # Agrupa por mes
            .annotate(count=Count('id'))  # Cuenta las publicaciones en ese mes
            .order_by('-month')  # Ordena por mes descendente
        )

        # Crear una lista de meses con publicaciones
        month_names = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }
        post_by_month_list = [
            f"{month_names[post['month'].month]} {post['month'].year}"
            for post in posts_by_month
        ]

        # Añadir la lista de meses al contexto
        context["post_by_month"] = post_by_month_list

        # Leer el archivo JSON de curiosidades
        json_path = os.path.join(settings.BASE_DIR, 'static/json/curiosidades-hacking.json')
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                curiosities = json.load(file).get("curiosidades", [])
                # Seleccionar una curiosidad al azar
                context["curiosity_hacking"] = random.choice(curiosities) if curiosities else "No hay curiosidades hacking disponibles."
        except (FileNotFoundError, json.JSONDecodeError) as e:
            context["curiosity_hacking"] = "No se pudo cargar la curiosidad debido a un error."

        json_path2 = os.path.join(settings.BASE_DIR, 'static/json/curiosidades-django.json')
        try:
            with open(json_path2, 'r', encoding='utf-8') as file:
                djangoFactsAndProjects = json.load(file).get("DjangoFactsAndProjects", [])
                # Seleccionar una curiosidad al azar
                context["curiosity_django"] = random.choice(djangoFactsAndProjects) if djangoFactsAndProjects else "No hay curiosidades disponibles."
        except (FileNotFoundError, json.JSONDecodeError) as e:
            context["curiosity_django"] = "No se pudo cargar la curiosidad debido a un error."    

        return context

    
class HackingMapView(ListView):
    model = Hacked
    template_name = 'home/hacking.html'
    context_object_name = 'data'
    
class ArticleDetailView(DetailView):
    model = Post # Especifica el modelo Blog
    template_name = 'home/article_detail.html' # Define el template "articulo_completo.html"
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Agregamos el formulario al contexto
        context['comments'] = Comment.objects.filter(post=self.object)  # Filtra comentarios por el post actual
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Obtén el objeto actual del post
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object  # Asocia el comentario al post actual
            comment.user = request.user  # Asocia el comentario al usuario autenticado
            comment.save()
            return redirect('home_app:article_detail', pk=self.object.pk)  # Redirige al detalle del artículo
        # Si el formulario no es válido, vuelve a renderizar la página con el formulario
        context = self.get_context_data()
        context['form2'] = form
        return self.render_to_response(context)


class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Post  # Especifica el modelo relacionado
    form_class = PostForm  # Usa form_class para asociar el formulario personalizado
    template_name = 'home/article_create.html'  # Especifica la plantilla para la vista
    success_url = reverse_lazy('home_app:home')

    def test_func(self):
        return self.request.user.is_staff

class ArticleUpdateView(UserPassesTestMixin, UpdateView):
    model = Post  # Especifica el modelo relacionado
    form_class = PostForm  # Usa form_class para asociar el formulario personalizado
    template_name = 'home/article_create.html'  # Especifica la plantilla para la vista
    success_url = reverse_lazy('home_app:home')
    
    def test_func(self):
        return self.request.user.is_staff

def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Asignar el usuario autenticado
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    
    return render(request, 'comments/add_comment.html', {'form': form, 'post': post})




class ContactView(TemplateView):
    template_name = 'home/contact.html'

    
class ContactView(FormView):
    template_name = 'home/contact.html'  # Nombre de tu plantilla
    form_class = ContactForm
    success_url = reverse_lazy('contacto_exito')  # Redirige a una página de éxito

    def form_valid(self, form):
        # Procesar el formulario (por ejemplo, enviar un correo)
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']

        # Opcional: enviar un correo electrónico
        send_mail(
            subject=f'Mensaje de {nombre}',  # Asunto del correo
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Correo configurado en settings
            recipient_list=[settings.CONTACT_EMAIL],  # Destinatario (correo de contacto)
            fail_silently=False,
        )

        return super().form_valid(form)


class PruebaEmail(FormView):
    def get(self, request, *args, **kwargs):
        message = Mail(
            from_email='from_email@example.com',
            to_emails='to@example.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>'
        )
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return HttpResponse("Correo enviado exitosamente.")  # Respuesta exitosa
        except Exception as e:
            print(str(e))
            return HttpResponse("Error al enviar el correo.", status=500) 


class AboutView(TemplateView):
    template_name = 'home/about.html'

class CookiesPolicyView(TemplateView):
    template_name = 'home/cookies_policy.html'

class ProvacyPolicyView(TemplateView):
    template_name = 'home/privacy_policy.html'

class LegalPoliciesView(TemplateView):
    template_name = 'home/legal_policies.html'


#celery
# applications/home/views.py


def trigger_task(request):
    result = example_task.delay(4, 6)  # Ejecuta la tarea en segundo plano
    return JsonResponse({'task_id': result.id, 'status': 'Task triggered!'})


  