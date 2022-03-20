from django.contrib import admin
from .models import record
# Register your models here.

@admin.register(record)
class record_display(admin.ModelAdmin):

    list_display=['name','id','email']
