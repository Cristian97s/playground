from django.shortcuts import render
from datetime import date
# Create your views here.

def home(request):
    today = date.today()
    stock = ['Django', 'Frappe', 'FastApi', 'Dotnet', 'Vue', 'React', 'python', 'csharp', 'javascript', 'sql']
    return render(request, "landing/landing.html", {
        "name": "Crist",
        "today": today,
        "age": 28,
        "stock": stock
    })