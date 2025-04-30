from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
