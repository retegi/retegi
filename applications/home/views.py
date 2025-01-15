from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post, Technology, Comment, Hacked
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.utils.dateformat import format
from django.contrib.auth.mixins import UserPassesTestMixin

class HomePageView(ListView):
    template_name = "home/index.html"
    model = Post
    context_object_name = 'entradas_blog'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["post_list"] = Post.objects.all()
        context["technology_list"] = Technology.objects.all()
        context["hacked_victims"] = Hacked.objects.all()
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

        # Añadir la lista al contexto
        context["post_by_month"] = post_by_month_list
        return context
    
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
        context['form'] = form
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

class AboutView(TemplateView):
    template_name = 'home/about.html'

class CookiesPolicyView(TemplateView):
    template_name = 'home/cookies_policy.html'

class ProvacyPolicyView(TemplateView):
    template_name = 'home/privacy_policy.html'

class LegalPoliciesView(TemplateView):
    template_name = 'home/legal_policies.html'

  