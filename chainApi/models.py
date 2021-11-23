from django.db import models

class GoalTime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    userName = models.CharField(max_length=100,blank=True,default='こすこす')
    userId = models.IntegerField(blank=True,default=0)
    todayGoal = models.BigIntegerField(blank=True,default=0)
    todayNow = models.BigIntegerField(blank=True,default=0)
    weekGoal = models.BigIntegerField(blank=True,default=0)
    weekNow = models.BigIntegerField(blank=True,default=0)

    class Meta:
        ordering = ['created']
