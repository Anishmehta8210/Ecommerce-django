from django.shortcuts import render

# Create your views here.
def home(r):
    return render(r,"index.html")

def login(r):
    return render(r,"login.html")
