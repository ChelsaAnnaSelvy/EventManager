from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

class EventDetails(models.Model):
    event_id = models.BigAutoField(primary_key=True, default=100000)
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images/', null=True, blank=True)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    speaker_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    is_online = models.BooleanField(default=False)
    video_link = models.URLField(blank=True, null=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seats_available = models.IntegerField(null=True, blank=True)

    def clean(self):
        cleaned_data = super().clean()
        is_online = cleaned_data.get('is_online', False)
        video_link = cleaned_data.get('video_link', '')

        if is_online and not video_link:
            self.add_error('video_link', 'This field is required when the event is online.')

        start_datetime = datetime.combine(datetime.today(), self.start_time)
        end_datetime = datetime.combine(datetime.today(), self.end_time)

        duration = end_datetime - start_datetime

        if duration > timedelta(hours=2):
            raise ValidationError("The duration of events should not exceed 2 hours")
