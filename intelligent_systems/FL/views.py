from django.shortcuts import render

# Create your views here.
def migration_FL_View(request):
    return render(request, 'migration_FL.html', {})
