from django.urls import path
from .views import login_user, user_home, view_events, add_event, edit_event
urlpatterns=[
    
    path('', login_user, name='sign_in'),
    path('home/', user_home, name='user_home'),
    path('event/', view_events, name='event_details'),
    path('create_event/', add_event, name='add_event'),
    path('modify_event/', edit_event, name='edit_event')




]