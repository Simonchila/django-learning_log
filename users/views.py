from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_user(request):
    logout(request)
    return redirect('learning_logs:index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(request=request, username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('learning_logs:index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def logout_user(request):
    logout(request)
    return redirect('learning_logs:index')