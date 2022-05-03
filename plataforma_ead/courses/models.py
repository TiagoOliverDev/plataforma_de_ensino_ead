from distutils.command import upload
from email.mime import image
from pyexpat import model
from tracemalloc import start
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
#from django.forms import CharField

# Create your models here.

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | \
        models.Q(description__icontains=query)
    )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o curso', blank=True) #descrição completa
    start_date = models.DateField('Data de início', null=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)  #Criado em
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)  #Atualizado em
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    objects = CourseManager() # agr o .objects será o personalizado

    def __str__(self) -> str:
        return self.name

  
    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)]) #id referente ao id passado na url details


    class Meta: 
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

    
  

    