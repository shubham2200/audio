from django.db import models
# from django.core.validators import FileExtensionValidator
# Create your models here.
from datetime import datetime

class Songs(models.Model):
    # today = 
   

    song_name = models.FileField(blank=True, max_length=100, upload_to='media/')
    duration = models.CharField(max_length=20)
    uploaded_time = models.DateTimeField(auto_created=True)
    # def __str__(self):
    #     return self.song_name
