from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.http import HttpResponse


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




def login(request):
    return render(request, 'account/login.html')


