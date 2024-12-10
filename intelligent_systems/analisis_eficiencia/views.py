from django.shortcuts import render
from academico import utils as utils_academico
# from intelligent_systems.academico import urls as utils_academico

# Create your views here.
def analisis_Eficiencia_View(request):
    # profesores = utils_academico.get_profesor_list()
    values_profesores=utils_academico.obtener_datos_encuestas()
    context={'data': values_profesores}
    return render(request, 'analisis_comparativo.html', context)