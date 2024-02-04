from django.db import models
from django.contrib.auth.models import User
from datetime import tim

# Create your models here.

class EventDetails(models.Model):
    event_id = models.BigAutoField(primary_key = True,default = 100000)
    title = models.CharField(max_length = 200, null = False)
    description = models.TextField(null = False)
    featured_image = models.ImageField(upload_to = 'featured_images/', null = True, blank = True)
    event_date= models.DateField(null = False)
    start_time = models.TimeField(null = False)
    end_time = models.TimeField(null = False)
    speaker_names = models.CharField(max_length = 200, null = False)
    subject = models.CharField(max_length = 200, null = True, blank = True)
    is_published = models.BooleanField(default = True)
    is_online = models.BooleanField(default = False)
    video_link = models.URLField(blank = True, null = True)
    last_updated_by = models.ForeignKey(User,on_delete = models.SET_NULL, null = True)
    seats_available = models.IntegerField(null = True, blank = True)



