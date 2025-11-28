from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import SolicitudAnalisis, Muestra
from .forms import SolicitudAnalisisForm, MuestraForm

def inicio(request):
    return render(request, 'analisis/inicio.html')

def about(request):
    return render(request, 'analisis/sobre-mi.html')

@login_required
def crear_solicitud(request):
    if request.method == "POST":
        form = SolicitudAnalisisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Solicitud creada correctamente.")
            return redirect('analisis:listar-solicitudes')
    else:
        form = SolicitudAnalisisForm()
    return render(request, 'analisis/crear-solicitud.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def listar_solicitudes(request):
    solicitudes = SolicitudAnalisis.objects.all()
    return render(request, 'analisis/listar-solicitudes.html', {'solicitudes': solicitudes})


# ----- Muestras (CBV) -----

class MuestraListView(ListView):
    model = Muestra
    template_name = 'analisis/listado-muestra.html'
    context_object_name = 'muestras'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(codigo_id_muestra__icontains=q) | qs.filter(raza__icontains=q)
            if not qs.exists():
                messages.warning(self.request, "No se encontraron muestras creadas.")
        return qs

class MuestraDetailView(DetailView):
    model = Muestra
    template_name = 'analisis/detalle-muestra.html'

class MuestraCreateView(LoginRequiredMixin, CreateView):
    model = Muestra
    form_class = MuestraForm
    template_name = 'analisis/muestra_form.html'
    success_url = reverse_lazy('analisis:listado-muestra')

class IsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return True

class MuestraUpdateView(LoginRequiredMixin, IsOwnerMixin, UpdateView):
    model = Muestra
    form_class = MuestraForm
    template_name = 'analisis/muestra_form.html'
    success_url = reverse_lazy('analisis:listado-muestra')

class MuestraDeleteView(LoginRequiredMixin, IsOwnerMixin, DeleteView):
    model = Muestra
    template_name = 'analisis/muestra_confirm_delete.html'
    success_url = reverse_lazy('analisis:listado-muestra')

# ----- Solicitudes (CBV) -----

class SolicitudDetailView(DetailView):
    model = SolicitudAnalisis
    template_name = 'analisis/detalle-solicitud.html'


class SolicitudUpdateView(LoginRequiredMixin, UpdateView):
    model = SolicitudAnalisis
    form_class = SolicitudAnalisisForm
    template_name = 'analisis/solicitud_form.html'
    success_url = reverse_lazy('analisis:listar-solicitudes')


class SolicitudDeleteView(LoginRequiredMixin, DeleteView):
    model = SolicitudAnalisis
    template_name = 'analisis/solicitud_confirm_delete.html'
    success_url = reverse_lazy('analisis:listar-solicitudes')
