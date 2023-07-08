from django.contrib import admin

# Register your models here.

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product_name','rating', 'comment', 'date_created')

