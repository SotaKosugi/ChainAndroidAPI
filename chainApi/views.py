from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chainApi.models import GoalTime
from chainApi.serializers import GoalSerializer

@api_view(['GET', 'POST'])
def goaltime_list(request,format=None):

    if request.method == 'GET':
        goaltime = GoalTime.objects.get(userId=0)
        serializer = GoalSerializer(goaltime)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #オブジェクトが既に存在していればデータを更新する
        if GoalTime.objects.filter(userId=0).exists():
            goaltime = GoalTime.objects.get(userId=0)
            serializer = GoalSerializer(data=request.data, instance=goaltime)
        #オブジェクトが存在してなければオブジェクトを作成する
        else:
            serializer = GoalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
