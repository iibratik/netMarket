from django.shortcuts import render, redirect
from .forms import UserForm

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:main')  
    else:
        form = UserForm()
        
    return render(request, 'main/account.html', {'form': form})