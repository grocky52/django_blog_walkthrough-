from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import userRegisterForm
from django.contrib.auth.decorators import login_required
from . forms import userupdateform, profileupdateform
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account created successfuly and you are ready to log in')
            return redirect('login')

            
    else:
        form = userRegisterForm()

    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST, instance = request.user)
        p_form = profileupdateform(request.POST, request.FILES, instance= request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'your profile has been successfuly updated')
            return redirect('profile')

    else:
        u_form = userupdateform(instance = request.user)
        p_form = profileupdateform(instance= request.user.profile)


    context ={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'users/profile.html', context)