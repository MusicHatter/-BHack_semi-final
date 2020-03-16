from django.shortcuts import render
from .models import Info_user




def home(request):

    return render(request, 'homepage/home.html')
