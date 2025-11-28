from django.db import models

class SolicitudAnalisis(models.Model):

    TIPOS_SOLICITUD = [
        ('padre', 'Verificación con padre'),
        ('padre_madre', 'Verificación con padre y madre'),
        ('buscar_padre', 'Búsqueda de padre'),
        ('buscar_madre', 'Búsqueda de madre'),
    ]

    TIPOS_MUESTRA = [
        ('sangre', 'Sangre'),
        ('pelo', 'Pelo'),
        ('saliva', 'Saliva'),
        ('hisopado', 'Hisopado'),
        ('otro', 'Otro'),
    ]

    nombre_solicitante = models.CharField(max_length=100)
    email_solicitante = models.EmailField()
    tipo_solicitud = models.CharField(max_length=20, choices=TIPOS_SOLICITUD)
    tipo_muestra = models.CharField(max_length=20, choices=TIPOS_MUESTRA)
    fecha_solicitud = models.DateField(auto_now_add=True)
    datos_adicionales = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.tipo_solicitud}"


class Muestra(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]

    codigo_id_muestra = models.CharField(max_length=20, unique=True)  # antes 50
    raza = models.CharField(max_length=100)
    RP = models.CharField(max_length=10, blank=True, null=True)      # opcional, solo números
    BU = models.CharField(max_length=7, blank=True, null=True)       # opcional, max 7
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    imagen_muestra = models.ImageField(upload_to="muestras/", blank=True, null=True)

    def __str__(self):
        return f"Muestra {self.codigo_id_muestra}"
