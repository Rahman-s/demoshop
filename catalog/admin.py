from django.contrib import admin
from .models import Shoe

# Dashboard ko professional banane ke liye
@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'is_available', 'created_at')
    fields = ('name', 'brand', 'description', 'price', 'image', 'banner_video', 'is_available')
    list_filter = ('brand', 'is_available')
    search_fields = ('name', 'brand')
    list_editable = ('price', 'is_available') # Owner list se hi price change kar sakta hai

# Register your models here.
