from django.contrib import admin
from .models import *

# Register your models here.
# class studentadmin(admin.ModelAdmin):
#     list_display=['name','email','phoneno']



class employeeadmin(admin.ModelAdmin):
    list_display=['name','email','password']
    
admin.site.register(employee,employeeadmin)
    



