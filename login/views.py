from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from registration.models import Regular_User
from .forms import UserForm

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                regular_user = Regular_User.objects.get(username=username, password=password)
                user, created = User.objects.get_or_create(username=regular_user.username)
                if created:
                    user.set_password(password)
                    user.save()
                login(request, user)
                return redirect('main:main')
            except Regular_User.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserForm()

    return render(request, 'main/login.html', {'form': form})