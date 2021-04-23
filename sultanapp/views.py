from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sultan(request):
    return HttpResponse("<h1>Hello pakistan</h1>")