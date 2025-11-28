from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SolicitudAnalisis, Muestra

admin.site.register(SolicitudAnalisis)
admin.site.register(Muestra)
