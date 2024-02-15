from django.urls import path
from .views import login_user, user_home, view_events,add_events
urlpatterns=[
    
    path('',login_user,name='sign_in'),
    path('home/',user_home,name='user_home'),
    path('event/',view_events,name='event_details'),
    path('addevent/',add_events,name='add_event'),


]