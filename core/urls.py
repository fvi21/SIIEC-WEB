from django.urls import path
from django.contrib.auth.views import LoginView 
from django.contrib.auth import views as auth_views
from.import views
#aca genero las urls que va a tener la app core de nuestro proyecto 
urlpatterns = [

    #path del core
    path('principal/', views.home, name="home"),
    path('formpaciente/', views.fomPaciente, name="form"),
    path('cargapaciente/', views.cargaPacientes, name="pacienteform"),
    path('', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]