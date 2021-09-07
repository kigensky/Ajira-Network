from django.contrib import admin
from .models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    exclude = ("creater",)
    list_display = ("position_name","creater",)
    
    def save_model(self, request, obj, form, change):
        obj.creater = request.user
        obj.save()

admin.site.register(Job, JobAdmin)

