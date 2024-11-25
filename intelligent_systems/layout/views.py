from django.shortcuts import render
from AST.views import migration_AST_View
from FL.views import migration_FL_View

# Create your views here.
def homeLayout(request):
    return render( request, 'sidebar.html', {})

def migration_AST(request):
    return migration_AST_View(request)

def migration_FL(request):
    return migration_FL_View(request)