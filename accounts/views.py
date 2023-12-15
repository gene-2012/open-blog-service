from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """
    Some thing went wrong.
    We need you to help us to fix it.
    So we closed this page.
    """
    return HttpResponse('Sorry, for the safety we closed this page.')
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.page = f'this is {new_user.username}\'s page'
            new_user.save()
            login(request, new_user)
            return redirect('blogs:index')
    context = {'form' : form}   
    return render(request, 'registration/register.html', context)