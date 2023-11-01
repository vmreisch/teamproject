from .models import Athlete
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = Athlete
        
        fields = ['id', 'name', 'jersey_number', 'position', 'salary', 'years_left_on_contract']
