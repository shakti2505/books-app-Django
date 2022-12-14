from django.shortcuts import render, redirect
# importing UserCreationForm to build the authentication form 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    #checking if request is POST
    if request.method =='POST':
        # if request is post then saving the request in the form 
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        # checking the validation of the form
        if form.is_valid():
            #saving the form data
            form.save()
            # extracting the user name from the form to use is while displaying the message
            username = form.cleaned_data.get('username')
            #displaying the message after successful singup
            messages.success(request, f'Welcome {username} , Your account is created.')
            # redirecting to the index page 
            return redirect('login')

    else:    
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile_page(request):
    return render(request, 'users/profile.html')




