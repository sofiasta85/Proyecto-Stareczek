from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='acceder'),
    path('logout/', views.logout_view, name='cerrar_sesion'),
]
