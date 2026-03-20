from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
# Create your views here.

def home(request):
    today = date.today()
    stock = [ {'id':'Django', 'name': 'Django'}, 
             {'id':'Frappe', 'name': 'Frappe'}, 
             {'id':'FastApi', 'name': 'FastApi'}, 
             {'id':'Dotnet', 'name': 'Dotnet'}, 
             {'id':'Vue', 'name': 'Vue'}, 
             {'id':'React', 'name': 'React'}, 
             {'id':'python', 'name': 'python'}, 
             {'id':'csharp', 'name': 'csharp'}, 
             {'id':'javascript', 'name': 'javascript'}, 
             {'id':'sql', 'name': 'sql'},]
    return render(request, "landing/landing.html", {
        "name": "Crist",
        "today": today,
        "age": 28,
        "stock": stock
    })

def stack_detail(request, tool):
    return HttpResponse(f"Tecnologia: {tool}")