from django.shortcuts import render
from rest_framework import viewsets
from trabalho.models import Trabalho
from trabalho.serializer import TrabalhoSerializer


class TrabalhoViewSet(viewsets.ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer
