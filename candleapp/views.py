from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'candleapp/index.html')

def about(request):
	return render(request, 'candleapp/about.html')

def shop(request):
	return render(request, 'candleapp/shop.html')

def contact(request):
	return render(request, 'candleapp/contact.html')


