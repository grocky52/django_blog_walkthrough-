from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import userRegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'account created successfuly for {user}')
            return redirect('blog:home')

            
    else:
        form = userRegisterForm()

    return render(request, 'users/register.html', {'form':form})