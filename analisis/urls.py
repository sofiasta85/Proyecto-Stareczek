from django.urls import path
from . import views

app_name = 'analisis'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='sobre-mi'),

    # solicitudes
    path('solicitudes/crear/', views.crear_solicitud, name='crear-solicitud'),
    path('solicitudes/', views.listar_solicitudes, name='listar-solicitudes'),

    # muestras
    path('muestras/', views.MuestraListView.as_view(), name='listado-muestra'),
    path('muestras/crear/', views.MuestraCreateView.as_view(), name='crear-muestra'),
    path('muestras/<int:pk>/', views.MuestraDetailView.as_view(), name='detalle-muestra'),
    path('muestras/<int:pk>/editar/', views.MuestraUpdateView.as_view(), name='editar-muestra'),
    path('muestras/<int:pk>/borrar/', views.MuestraDeleteView.as_view(), name='borrar-muestra'),
    path('solicitudes/<int:pk>/', views.SolicitudDetailView.as_view(), name='detalle-solicitud'),
    path('solicitudes/<int:pk>/editar/', views.SolicitudUpdateView.as_view(), name='editar-solicitud'),
    path('solicitudes/<int:pk>/borrar/', views.SolicitudDeleteView.as_view(), name='borrar-solicitud'),

]
