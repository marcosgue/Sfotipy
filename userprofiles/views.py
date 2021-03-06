from django.shortcuts import render
from django.contrib.auth import login

from .forms import UserCreationEmailForm, EmailAuthenticationForm


def singup(request):
    form = UserCreationEmailForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'singup.html', {'form': form})


def singin(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        login(request, form.get_user())

    return render(request, 'singin.html', {'form': form})
