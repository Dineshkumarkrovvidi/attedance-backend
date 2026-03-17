from django.shortcuts import render
from rest_framework import viewsets
from .models import Takeattedence
from .serializer import Attendance1Serializer
# Create your views here.
class TakeAttedenceView(viewsets.ModelViewSet):
    queryset = Takeattedence.objects.all()
    serializer_class=Attendance1Serializer