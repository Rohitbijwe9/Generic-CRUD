from django.shortcuts import render
from .models import Studet
from .serializer import StudentSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView



class AddShow(CreateAPIView,ListAPIView):
    serializer_class=StudentSerializer
    queryset=Studet.objects.all()


class updel(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=StudentSerializer
    queryset=Studet.objects.all()
    