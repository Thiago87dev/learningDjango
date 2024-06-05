# from django.http import HttpResponse
from django.shortcuts import render

context = {
    'text' : 'Estamos na home ',
    'title' : 'Home - ',
    'css' : 'home/css/blue.css',
    }
def home(req):
    return render(req, 'home/index.html', context)
