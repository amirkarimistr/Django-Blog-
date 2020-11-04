from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your account has been created {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

@login_required()
def profile(request):

    return render(request, 'users/profile.html')

