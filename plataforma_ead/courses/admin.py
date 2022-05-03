from re import search
from django.contrib import admin
# Register your models here.
# primeiro importa o models que queremos cadastrar aqui no admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at'] # o que será exibido na tela do admin
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} #deixando slug com preenchimento automático!

admin.site.register(Course, CourseAdmin)


