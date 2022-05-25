from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import userRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account created successfuly and you are ready to log in')
            return redirect('blog:login')

            
    else:
        form = userRegisterForm()

    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')