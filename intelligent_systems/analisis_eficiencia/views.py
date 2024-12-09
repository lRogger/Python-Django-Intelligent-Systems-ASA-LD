from django.shortcuts import render
# from intelligent_systems.academico import urls as utils_academico

# Create your views here.
def analisis_Eficiencia_View(request):
    # profesores = utils_academico.get_profesor_list()
    # context={'profesores': profesores}
    return render(request, 'analisis_comparativo.html', {})