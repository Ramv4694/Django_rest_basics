from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required



from .models import Language
from .serializers import LanguageSerializer

# Create your views here.
@login_required()
class LanguageView(viewsets.ModelViewSet):
    queryset =  Language.objects.all()
    serializer_class = LanguageSerializer
