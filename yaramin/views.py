from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    templates = loader.get_template('base.html')
    return HttpResponse(templates.render())

def log_in(request):
    templates = loader.get_template('login.html')
    return HttpResponse(templates.render())

def sign_up(request):
    templates = loader.get_template('signup.html')
    return HttpResponse(templates.render())

def show_computers(request):
    templates = loader.get_template('computers.html')
    return HttpResponse(templates.render())

def show_tablets(request):
    templates = loader.get_template('tablets.html')
    return HttpResponse(templates.render())

def show_mobiles(request):
    templates = loader.get_template('mobiles.html')
    return HttpResponse(templates.render())

def show_products(request, phone):
    value={
        'productName':phone
    }

    templates = loader.get_template('products.html')
    return HttpResponse(templates.render(value))