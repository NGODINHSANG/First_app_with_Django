from collections import namedtuple
from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(reponse, id):

    ls = ToDoList.objects.get(id=id)
    if reponse.user.todolist.all():
        if reponse.method == "POST":
            print(reponse.POST)
            if reponse.POST.get("save"):
                for item in ls.item_set.all():
                    if reponse.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif reponse.POST.get("newItem"):
                txt = reponse.POST.get("new")

                if len(txt) > 2 :
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")

        return render(reponse, "main/list.html", {"ls":ls})
    return render(reponse, "main/view.html", {})

def home(reponse):
    return render(reponse, "main/home.html", {})

def create(reponse):
    if reponse.method == "POST":
        form = CreateNewList(reponse.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            reponse.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    form = CreateNewList()
    return render(reponse, "main/create.html", {"form":form})

def view(reponse):
    return render(reponse, 'main/view.html', {})