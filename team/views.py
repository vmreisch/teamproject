from .models import Athlete
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AthleteSerializer

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.AllowAny]