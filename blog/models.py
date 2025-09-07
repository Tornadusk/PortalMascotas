# ⚠️ NOTA: Este modelo tiene dependencias de MongoDB que NO se deben usar en este proyecto
# Las importaciones de django_mongodb_backend generan error porque no está instalado
# Este archivo está comentado/deshabilitado para evitar errores del servidor
# Si se necesita usar el blog, cambiar la forma en que trabaja el modelo o instalar: pip install django-mongodb-backend
# En nuestro caso actual NO se debe usar este modelo
#
# 📝 NOTA ADICIONAL: Este modelo también usa el campo 'author' que referencia a AUTH_USER_MODEL
# Si se habilita el blog, asegurarse de que funcione correctamente con el modelo Usuario personalizado

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import ArrayField, EmbeddedModelArrayField

class Comment(EmbeddedModel):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

STATUS_CHOICES = (("draft", "Borrador"), ("published", "Publicado"))

class Post(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    content = models.TextField()
    tags = ArrayField(models.CharField(max_length=32), blank=True, null=True)
    hero_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    published_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = EmbeddedModelArrayField(embedded_model=Comment, blank=True, null=True)

    class Meta:
        db_table = "blog_posts"
        indexes = [
            models.Index(fields=["-published_at"]),
            models.Index(fields=["category", "-published_at"]),
            models.Index(fields=["slug"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title