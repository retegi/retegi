from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField



class Technology(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img', blank=True, null=True)

    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.name     

class Post(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()
    summary = HTMLField( blank=True,null=True)
    technology = models.ManyToManyField(Technology, blank=True)
    github = models.URLField(max_length=300, blank=True,null=True)
    #video = models.URLField(max_length=300, blank=True,null=True)
    video = models.URLField(max_length=300, blank=True,null=True)

    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.title

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.summary[:200]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content2 = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
class Hacked(models.Model):
    image = models.ImageField(upload_to='img/hacking/victims/', blank=True, null=True)
    victim = models.CharField(max_length=255,null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    date_time2 = models.DateTimeField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    latitude = models.CharField(max_length=255,null=True, blank=True)
    longitude = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    technique = models.TextField(null=True, blank=True)
    hacker_name = models.CharField(max_length=255,null=True, blank=True)
    hacker_captured = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    locality = models.CharField(max_length=255,null=True, blank=True)
    province = models.CharField(max_length=255,null=True, blank=True)
    autonomous_comumnity = models.CharField(max_length=255,null=True, blank=True)
    country = models.CharField(max_length=255,null=True, blank=True)
    hacker_locality_latitude = models.CharField(max_length=255,null=True, blank=True)
    hacker_locality_longitude= models.CharField(max_length=255,null=True, blank=True)

    def __stre__(self):
        return str(self.victim)
    
