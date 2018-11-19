from django.shortcuts import render, redirect, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
   
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created succesfully! Please log in') # Flash message of type messages.success
            return redirect('login')
    else: 
        form = UserRegisterForm() 
    return render(request, 'users/register.html', {'form':form})

@login_required # Django makes it easy to make sure that only logged in users can view this view
def profile(request):
    return render(request, 'users/profile.html')
