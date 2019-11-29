from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nokia(request):
    return render(request, "itcompany/hello.html")