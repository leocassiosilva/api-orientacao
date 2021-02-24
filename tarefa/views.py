from django.shortcuts import render
from rest_framework import viewsets
from tarefa.models import Tarefa
from tarefa.serializer import TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
