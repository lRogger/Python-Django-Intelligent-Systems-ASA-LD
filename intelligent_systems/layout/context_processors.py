# layout/context_processors.py

from django.urls import reverse

def sidebar_items(request):
    # Define el arreglo de los items del sidebar
    sidebar_items = [
        {
            'name': 'Migraciones',
            'url': reverse('migration_excel'),
            'icon': 'M10.5 6...',
            'active_url': '/modules/migration/',
        },
        {
            'name': 'Análisis de Eficiencia',
            'url': reverse('analisis_eficiencia'),
            'icon': 'M10.5 6...',
            'active_url': '/modules/analisis-eficiencia/',
        },
        {
            'name': 'Compatibilidad por Docente',
            'url': reverse('analisis_docente'),
            'icon': 'M10.5 6...',
            'active_url': '/modules/analisis-docente/',
        },
        {
            'name': 'Docentes asignados',
            'url': reverse('docentes_asignados'),
            'icon': 'M10.5 6...',
            'active_url': '/modules/docentes-asignados/',
        },
    ]
    return {'sidebar_items': sidebar_items}
