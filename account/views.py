from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout



def home(request):
    return render(request, 'account/index.html')



def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully')
        
    context = {'form': form}
            # return redirect('login')
    return render(request, 'account/register.html', context=context)




def user_login(request):


    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_writer==True:
                auth_login(request, user)
                return redirect('writer_dashboard')
            if user is not None and user.is_writer==False:
                auth_login(request, user)
                return redirect('client_dashboard')
            
    context = {'form': form}

    return render(request, 'account/login.html', context=context)



def user_logout(request):
    auth_logout(request)
    return redirect('home')