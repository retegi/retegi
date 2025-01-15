from django import forms
from .models import Post, Technology, Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    technology = forms.ModelMultipleChoiceField(
        queryset=Technology.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Widget para selección múltiple con checkboxes
        required=False,  # Opcional, ya que lo has marcado como blank=True en el modelo
        label="Tecnologías relacionadas",
    )
    content = forms.CharField(
    widget=TinyMCE(attrs={
        'cols': 80,
        'rows': 30,
        'class': 'form-control',  # Clase adicional para estilo Bootstrap
    }),
    label="Contenido del post",
)

    summary = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 10}),
        required=False,
        label="Resumen del post",
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'author',
            'content',
            'summary',
            'technology',
            'github',
        ]
        labels = {
            'title': 'Título',
            'image': 'Imagen del post',
            'author': 'Autor',
            'content': 'Contenido',
            'summary': 'Resumen',
            'technology': 'Tecnologia',
            'github': 'Enlace a GitHub',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'technology': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'github': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content2']  # Campos que se mostrarán en el formulario
        labels = {
            'content2': 'Comentario',  # Etiqueta personalizada para el campo
        }
        widgets = {
            'content2': forms.Textarea(attrs={
                'class': 'form-control',  # Clase para estilos (Bootstrap u otro framework)
                'placeholder': 'Escribe tu comentario aquí...',
                'rows': 4,  # Número de filas del textarea
                'maxlength': 500,  # Máxima longitud del comentario
            }),
        }