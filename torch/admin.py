from django.contrib import admin
from .models import Code
# Register your models here.

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('created','is_read')
    list_filter = ('is_read',)
    
