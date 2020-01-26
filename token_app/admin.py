from django.contrib import admin
from .models import Token


class tokenAdmin(admin.ModelAdmin):
    list_display = ('key','state', 'created_at', 'updated_at', 'last_alive')

admin.site.register(Token, tokenAdmin)
