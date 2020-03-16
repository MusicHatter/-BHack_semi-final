from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import User_reg

def register(request):
    if request.method == "POST":
        form = User_reg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('auth')
    else:
        form = User_reg()
    return render(request, 'users/registration.html', {'form': form })


@login_required
def profile(request):
    return render(request, 'users/profile.html')
