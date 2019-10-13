from django.shortcuts import render, render_to_response
from . models import MyTable
# Create your views here.
def index(request):
    context = {
    'ID': MyTable.objects.all()
    }
    return(render(request, "index.html", context))
