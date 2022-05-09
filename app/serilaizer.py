from pyexpat import model
from .models import *
from rest_framework import serializers
# from django.db.models import fields
import os
from datetime import datetime

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = "__all__"
    def validate(self,attrs):
        song_name = attrs.get('song_name')
        duration = attrs.get('duration')
        uploaded_time = attrs.get('uploaded_time')
                
        # if not song_name.content-type in ["audio/mpeg","audio/..."]:
        #         raise serializers.ValidationError("Content-Type is not mpeg")
        if not os.path.splitext(song_name.name)[1] in  [".mp3",".wav" ,".wma" , ".amr" ]:
                raise serializers.ValidationError("Content-Type is should be mp3 ,mav , wma , amr")
        return attrs

    # def create(self, validated_data):
    #     now = datetime.now()
    #     user = Songs.objects.create(
    #         song_name=validated_data['song_name'],
    #         duration =validated_data['duration'],
    #         uploaded_time = validated_data[now]
    #     )
    #     return user

        
                


