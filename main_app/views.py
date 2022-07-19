from django.shortcuts import render

from django.http import HttpResponse

class Record:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, label, style, released, country):
    self.name = name
    self.label = label
    self.style = style
    self.released = released
    self.country = country

records = [
  Record('PHD & MC Conrad Progression Sessions / 3 By 4', 'Looking Good Records', 'Intelligent D&B', '1997', 'UK'),
  Record('Smith & Pledger - Believe', 'Anjuna', 'Trance', '2004', 'UK'),
  Record('Unknown Artist - UTIQUE 002', 'UTIQUE', 'Deep House', '2016', 'Germany')
]

def home(request):
    return HttpResponse('<h1>The home route is working :3</h1>')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    return render(request, 'records/index.html', { 'records': records })
