from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
db = client.HW_10


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if not db.users.find_one({"username": username}):
                db.users.insert_one({
                    "username": username,
                    "password": password,
                    "is_authenticated": True
                })

            return redirect("quotes:index")
        else:
            return HttpResponse("Невірний логін чи пароль")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("quotes:index")
