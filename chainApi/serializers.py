from rest_framework import serializers
from chainApi.models import GoalTime

class GoalSerializer(serializers.Serializer):
    userName = serializers.CharField(max_length=100,required=False)
    userId = serializers.IntegerField(required=False)
    todayGoal = serializers.IntegerField(default=0,required=False)
    todayNow = serializers.IntegerField(default=0,required=False)
    weekGoal = serializers.IntegerField(default=0,required=False)
    weekNow = serializers.IntegerField(default=0,required=False)

    def create(self,validated_data):
        return GoalTime.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.userName = validated_data.get('userName',instance.userName)
        instance.userId = validated_data.get('userId',instance.userId)
        instance.todayGoal = validated_data.get('todayGoal',instance.todayGoal)
        instance.todayNow = validated_data.get('todayNow',instance.todayNow)
        instance.weekGoal = validated_data.get('weekGoal',instance.weekGoal)
        instance.weekNow = validated_data.get('weekNow',instance.weekNow)
        instance.save()
        return instance