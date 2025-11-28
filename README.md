Descripción

Esta aplicación web desarrollada en Django permite la gestión de muestras de ADN y solicitudes de análisis para la verificación de parentesco en animales de producción.
Los usuarios pueden crear, editar, consultar y eliminar registros de manera segura, con autenticación de usuarios y una interfaz clara basada en templates heredados.

Funcionalidades principales

Gestión de Muestras: creación, edición, detalle y eliminación.
Gestión de Solicitudes: creación, edición, detalle y eliminación.
Autenticación de usuarios: registro, login y logout.
Mensajes de alerta: para búsquedas sin resultados o cuando no hay registros.
Subida de imágenes: permite asociar imágenes a las muestras.

Instalación rápida

Clonar el repositorio y entrar en la carpeta:

git clone <URL_DEL_REPOSITORIO>
cd mi_proyecto

Crear y activar un entorno virtual, instalar dependencias y aplicar migraciones:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate

Ejecutar el servidor:

python manage.py runserver

Abrir en el navegador: http://127.0.0.1:8000/

Autor

Sofía Stareczek – Magíster en Biología – Especialista en análisis de ADN y verificación de genealogía de animales de producción.