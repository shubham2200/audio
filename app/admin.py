from django.contrib import admin
from .models import *
# Register your models here.
class SongsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'song_name','uploaded_time')

admin.site.register(Songs , SongsAdmin)
