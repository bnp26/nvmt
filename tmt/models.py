from django.db import models

from psych.models import Test

class TmtTest(Test):
    pass

class Trial(models.Model):
    test = models.ForeignKey(TmtTest, related_name='trial', on_delete=models.CASCADE)
    trial_num = models.IntegerField(default=1)

    class Meta:
        unique_together = ('test', 'trial_num')
        ordering = ['trial_num']

class Card(models.Model):
    card_num = models.IntegerField(default=1)
    trial = models.ForeignKey(Trial, related_name='card', on_delete=models.CASCADE)

class Point(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    card = models.ForeignKey(Card, related_name='points', on_delete=models.CASCADE)
    click_order = models.IntegerField(default=0)
    click_time = models.DurationField(blank=True)