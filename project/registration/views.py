from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Regular_User

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            if Regular_User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already taken. Please choose a different one.')
            elif Regular_User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already taken. Please choose a different one.')
            else:
                form.save()
                return redirect('main:main')  
    else:
        form = UserForm()
        
    return render(request, 'main/account.html', {'form': form})