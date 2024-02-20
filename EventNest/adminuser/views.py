from django.shortcuts import render, redirect, get_object_or_404
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

def add_event(request):
    logged_user=request.user
    if request.method =='POST':
            form =AddEventForm(request.POST,request.FILES)
            if form.is_valid():
                new_event=form.save(commit=False)
                new_event.last_updated_by=logged_user
                new_event.save()
                messages.success(request, 'A new event is successfully added.')
                return redirect('event_details')
    else:
        form=AddEventForm()
    context={
        'logged_user':logged_user,
        'form': form,
        
    }
    return render(request,'adminuser/create_event.html',context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import EventDetails
from .forms import AddEventForm

def edit_event(request):
    logged_user = request.user   
    

    if request.method == 'POST': 
        event_id = request.POST.get('event_id', 0)
        event = get_object_or_404(EventDetails, event_id=event_id)   
        form = AddEventForm(request.POST, request.FILES, instance=event)  
        
        if form.is_valid():
            print('VALID')
            updated_event = form.save(commit=False)
            updated_event.last_updated_by = logged_user
            updated_event.save()
            messages.success(request, 'The selected event is successfully edited.')
            return redirect('event_details')
        else:            
            event_id = request.POST.get('event_id', 0)
            event = get_object_or_404(EventDetails, event_id=event_id)
            form = AddEventForm(instance=event)
            context = {
                'logged_user': logged_user,
                'form': form,
                'event_id':event_id
            }

    return render(request, 'adminuser/modify_event.html', context)

# def edit_event(request):
#     logged_user=request.user
    
#     if request.method =='POST':
#         event_id = request.POST.get('event_id', 0)    
#         event = get_object_or_404(EventDetails, event_id=event_id) 
#         form =AddEventForm(request.POST,request.FILES,instance=event)
#         if form.is_valid():
#             updated_event=form.save(commit=False)
#             updated_event.last_updated_by=logged_user
#             updated_event.save()
#             messages.success(request, 'The selected event is successfully edited.')
#             return redirect('event_details')
#         else:
#             event_id = request.POST.get('event_id', 0)    
#             event = get_object_or_404(EventDetails, event_id=event_id) 
#             form=AddEventForm(instance = event)
#             context={
#             'logged_user':logged_user,
#             'form': form,
            
#         }
#     return render(request,'adminuser/modify_event.html',context)

