from multiprocessing import context
from django.shortcuts import get_object_or_404, render


#from plataforma_ead import courses
from .models import Course
from .forms import ContactCourse
# Create your views here.

def index(request): 
    courses = Course.objects.all() #retornando todos os objetos cadastrados no banco de dodos
    template_name = 'courses/index.html'
    context = { 
        'courses': courses
    }
    return render (request, template_name, context) #context é um contexto na qual tem a variavel courses que tem todos os objetos do model course


#def detalhes(request, pk):
 #   course = get_object_or_404(Course, pk=pk) #.get retorna somente um de acordo com seu id (pk)
  #  return render (request, 'courses/details.html', {'course': course})


def details(request, id):
    course = get_object_or_404(Course, pk=id)#.get retorna somente um de acordo com seu id (pk)
    context = {
        'course': course
        #'form': ContactCourse()
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)




