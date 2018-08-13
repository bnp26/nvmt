from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from psych.models import Subject

class Test(models.Model):
    subject = models.ForeignKey(Subject, related_name='test', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

class Trial(models.Model):
    test = models.ForeignKey(Test, related_name='trials', on_delete=models.CASCADE)
    trial_num = models.IntegerField(default=1)

    class Meta:
        unique_together = ('test', 'trial_num')
        ordering = ['trial_num']

class Card(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    finish = models.DateTimeField()
    trial = models.ForeignKey(Trial, related_name='cards', on_delete=models.CASCADE)

class Target(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    card = models.ForeignKey(Card, related_name='targets', on_delete=models.CASCADE)
    is_goal = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True)
    clicked_at = models.DateTimeField(blank=True)
    click_time = models.DurationField(blank=True)
