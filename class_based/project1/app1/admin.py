from django.contrib import admin
from .models import StudentModel

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['rn','name','marks']

admin.site.register(StudentModel,StudentAdmin)    
