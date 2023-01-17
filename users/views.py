from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# from .models import Wallet
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
