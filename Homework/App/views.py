from django.shortcuts import render
from .forms import Form
from django.http import HttpResponseRedirect
from App.models import User


def join(request):
    if request.method == "POST":
        email = request.POST.get("email", "Undefined")
        password = request.POST.get("password", "Undefined")

        user = User.objects.get(email=email)

        if email == user.email and password == user.password:
            return render(request, 'result.html', context={'text': 'Вы успешно вошли'})

        else:
            return HttpResponseRedirect('registration/')

    else:
        form = Form()
        return render(request, 'join.html', {'form': form})


def registration(request):
    if request.method == "POST":
        name = request.POST.get("name", "Undefined")
        email = request.POST.get("email", "Undefined")
        password = request.POST.get("password", "Undefined")

        User.objects.create(login = name, password = password, email = email)
        return render(request, 'successfully.html', context={'name': name,'text': ', поздравляю с регистрацией!'})


    else:

        return render(request, 'registration.html', {'form': Form})


def user_return(request):
    return render(request, 'result.html')
