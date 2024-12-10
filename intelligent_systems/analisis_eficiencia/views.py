from django.shortcuts import render
from academico import utils as utils_academico
from django.contrib import messages
from FL import utils as utils_FL

# from intelligent_systems.academico import urls as utils_academico

# Create your views here.
def analisis_Eficiencia_View(request):
    # profesores = utils_academico.get_profesor_list()
    # try:
    #     # values_profesores=utils_academico.obtener_datos_encuestas()
    #     # fl_encuenta_profesores=utils_FL.logica_difusa_profesores(values_profesores)
    # except Exception as e:
    #     messages.error(request, str(e))
    # context={'fl_encuenta_profesores': fl_encuenta_profesores}
    return render(request, 'analisis_comparativo.html', {})