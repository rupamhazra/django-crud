from django.http import HttpResponse
from django.template import loader
from library.models import *
from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
from .forms import addbookForm

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def list_books(request):
  books = Books.objects.all().values()
  template = loader.get_template('library/list.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))

def add_book(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    # add the dictionary during initialization 
    form = addbookForm(request.POST or None) 
    if form.is_valid(): 
        form.save()
        template = loader.get_template('library/list.html')
        return redirect('books')

    context['form']= form 
    template = loader.get_template('library/add.html')
    return HttpResponse(template.render(context, request))
  
def details(request, id):
  book = Books.objects.get(id=id)
  template = loader.get_template('library/details.html')
  context = {
    'book': book,
  }
  return HttpResponse(template.render(context, request))

# update view for details
def bookEdit(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Books, id = id)
 
    # pass the object as instance in form
    form = addbookForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        template = loader.get_template('library/list.html')
        return redirect('books')
 
    # add form dictionary to context
    context["form"] = form
    template = loader.get_template('library/edit.html')
    return HttpResponse(template.render(context, request))