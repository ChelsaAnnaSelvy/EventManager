from django.contrib import admin
from .models import User, EventDetails
# Register your models here.



class EventAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(EventDetails,EventAdmin)