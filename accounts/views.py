from django.shortcuts import render,  redirect
# Importing FORM
from django.contrib.auth.forms import UserCreationForm
# Importing login
from django.contrib.auth import login
# Importing decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in automatically right now
            return redirect('home')
        
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form':form})

@login_required
def home_view(requests):
    return render(requests, 'accounts/home.html')