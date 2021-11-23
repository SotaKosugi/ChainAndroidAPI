from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from chainApi import views

urlpatterns =[
    path('chainApi/',views.goaltime_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)