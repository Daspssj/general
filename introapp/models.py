from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    def __str__(self):
        return self.title

class comentario(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comentarios')
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    active = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='coment_likes')
    def __str__(self):
        return f'comentario de {self.nombre}'
    def cantidad_likes(self):
        return self.likes.count