import requests
from django.shortcuts import render

def homepage(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    context = {
        "posts": data
    }
    
    return render(request, "myapp/homepage.html", context)

def todolist(request):
    return render(request, "myapp/todolist.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")