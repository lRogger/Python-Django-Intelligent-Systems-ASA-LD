from .models import Profesor


def get_profesor_list():
    profesores = Profesor.objects.all()
    return profesores