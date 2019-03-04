from django.shortcuts import render
from django.http import HttpResponse
from .forms import DMVForm, DMVModel, BankAccountForm, BankAccountModel
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return HttpResponse("Test URL")


def newUser(request):
    form = DMVForm(request.POST or None)
    context = {
        "form": form
    }

    if request.method == "POST":
        print(request.POST)
        User.objects.create_user(request.POST["IDNumber"], "", request.POST["password"])
        return render(request, "authenticationApp/welcomeNewUser.html")

    return render(request, 'authenticationApp/newUser.html', context)

def welcomeNewUser(request):
    return render(request, "authenticationApp/welcomeNewUser.html")


def newIndex(request):
    return render(request, "authenticationApp/newIndex.html")

def newBankUser(request):
    form = BankAccountForm(request.POST or None)
    context = {
        "form": form
    }

    if request.method == 'POST':
        User.objects.create_user(request.POST["username"], "", request.POST["password"])
        form.save()
        return HttpResponse("NEW USER CREATED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    return render(request, "authenticationApp/newBankUser.html", context)
