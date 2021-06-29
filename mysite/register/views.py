from django import forms
from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register(reponse):

    if reponse.method == 'POST':
        form = RegisterForm(reponse.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()
    return render(reponse, "register/register.html", {"form":form})
