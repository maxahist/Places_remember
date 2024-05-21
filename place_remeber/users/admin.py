from django.contrib import admin

from .models import User

@admin.register(User)
class RememberAdmin(admin.ModelAdmin):
    list_display = ('username',)
