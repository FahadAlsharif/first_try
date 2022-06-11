from django.http import HttpResponse
from django.shortcuts import redirect, render , HttpResponse

def root(request):
    return HttpResponse("this is the equivalent of @app.route('blog/')")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def num(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")
def edit(request,number):
    return HttpResponse(f"placeholder to edit blog number: {number}")
def destroy(request,number):
    return redirect('/blogs')