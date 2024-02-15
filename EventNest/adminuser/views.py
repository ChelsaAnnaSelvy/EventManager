from django.shortcuts import render, redirect
from .models import EventDetails, User
from .forms import LoginForm,AddEventForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']         
           
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home')            

        else:
            form = LoginForm()
            messages.error(request, 'Invalid username or password')
            return render(request, 'adminuser/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'adminuser/login.html', {'form': form})

@login_required   
def user_home(request):
    logged_user=request.user    
    return render(request,'adminuser/home.html',{'logged_user':logged_user})

def view_events(request):
    logged_user=request.user
    event_details=EventDetails.objects.all()
    context={
        'logged_user':logged_user,
        'event_details':event_details,
    }
    return render(request,'adminuser/event_details.html',context)

def add_events(request):
    logged_user=request.user
    if request.method =='POST':
            add_event_form =AddEventForm(request.POST,request.FILES)
            if add_event_form.is_valid():
                add_event_form.save()
                messages.success(request, 'A new event is successfully added.')
                return redirect('add_event')
    else:
        add_event_form=AddEventForm()
    context={
        'logged_user':logged_user,
        'form': add_event_form,
        
    }
    return render(request,'adminuser/add_events.html',context)

