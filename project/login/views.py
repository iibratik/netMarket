from django.shortcuts import render, redirect
from registration.models import Regular_User
from .forms import UserForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                regular_user = Regular_User.objects.get(username=username)
                if regular_user.password == password:
                    return redirect('main:main')
                else:
                    messages.error(request, 'Invalid username or password.')
            except Regular_User.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserForm()

    return render(request, 'main/login.html', {'form': form})