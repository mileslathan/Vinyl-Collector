from django.shortcuts import render
from .models import Record
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>The home route is working :3</h1>')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/detail.html', { 'record': record })

class RecordCreate(CreateView):
  model = Record
  fields = '__all__'
  success_url = '/records/'

class RecordUpdate(UpdateView):
    model = Record
    fields = ['label', 'style', 'released', 'country']

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'