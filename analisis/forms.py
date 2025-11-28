from django import forms
from .models import SolicitudAnalisis, Muestra

class SolicitudAnalisisForm(forms.ModelForm):
    class Meta:
        model = SolicitudAnalisis
        fields = "__all__"


class MuestraForm(forms.ModelForm):
    class Meta:
        model = Muestra
        fields = "__all__"
