from django.urls import path
from .views import *


urlpatterns=[
    path('addshow/',AddShow.as_view()),
    path('updel/<int:pk>/',updel.as_view())
]