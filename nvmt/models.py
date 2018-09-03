from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from psych.models import Test

import datetime

class NvmtTest(Test):
    def get_normative_data(self, age):
        norms = None
        if age >= 18 or age <= 20:
            norms = [{'mean': 48.29, 'sd': 7.032}, {'mean': 29.89, 'sd': 10.150}, {'mean':25.39, 'sd': 9.170}, {'mean': 21.82, 'sd': 8.030}, {'mean': 18.74, 'sd': 8.388}, {'mean': 16.05, 'sd': 6.251}]
        elif age >= 21 or age <= 30:
            norms = [{'mean': 49.34, 'sd': 9.725}, {'mean': 29.74, 'sd': 7.609}, {'mean': 24.77, 'sd': 9.735}, {'mean': 21.00, 'sd': 7.063}, {'mean': 19.06, 'sd': 7.025}, {'mean': 20.00, 'sd': 7.716}]
        elif age >= 31 or age <= 40:
            norms = [{'mean': 47.82, 'sd': 9.536}, {'mean': 30.03, 'sd': 8.926}, {'mean': 28.74, 'sd': 9.602}, {'mean': 24.21, 'sd': 9.380}, {'mean': 20.50, 'sd': 7.955}, {'mean': 20.53, 'sd': 6.999}]
        elif age >= 41 or age <= 50:
            norms = [{'mean': 46.75, 'sd': 7.442}, {'mean': 35.57, 'sd': 9.852}, {'mean': 30.32, 'sd': 10.822}, {'mean':30.04, 'sd': 12.926}, {'mean': 24.36, 'sd': 10.375}, {'mean': 25.36, 'sd': 10.552}]
        elif age >= 51 or age <= 60:
            norms = [{'mean': 50.12, 'sd': 7.928}, {'mean': 33.84, 'sd': 10.777}, {'mean': 30.76, 'sd': 10.449}, {'mean': 28.68, 'sd': 11.176}, {'mean': 24.12, 'sd': 7.923}, {'mean': 26.04, 'sd': 9.476}]
        elif age >= 61 or age <= 70:
            norms = [{'mean': 46.84, 'sd': 11.083}, {'mean': 32.47, 'sd': 10.357}, {'mean': 33.73, 'sd': 8.964}, {'mean': 30.07, 'sd': 10.320}, {'mean': 29.80, 'sd': 10.658}, {'mean':26.20, 'sd': 6.405}]
        elif age >= 71 or age <= 80:
            norms = [{'mean': 52.71, 'sd': 12.042}, {'mean': 41.71, 'sd': 11.124}, {'mean': 37.42, 'sd': 9.612}, {'mean': 35.84, 'sd': 8.952}, {'mean': 34.03, 'sd': 10.384}, {'mean': 31.81, 'sd': 10.572}]
        else:
            norms = None
        return norms
    
    def get_complex_data(self, age):
        norms = None
        if age >= 18 or age <= 20:
            norms = [{'mean': 27.66, 'sd': 5.454}, {'mean': 18.16, 'sd': 6.236}, {'mean': 17.82, 'sd': 7.307}, {'mean': 15.76, 'sd': 7.019}, {'mean': 12.61, 'sd': 6.954}, {'mean': 10.447, 'sd': 4.780}]
        elif age >= 21 or age <= 30:
            norms = [{'mean': 28.06, 'sd': 5.866}, {'mean': 18.40, 'sd': 5.730}, {'mean': 16.69, 'sd': 7.218}, {'mean': 13.91, 'sd': 4.961}, {'mean': 12.77, 'sd': 5.765}, {'mean': 12.743, 'sd': 5.517}]
        elif age >= 31 or age <= 40:
            norms = [{'mean': 47.82, 'sd': 6.347}, {'mean': 30.03, 'sd': 6.317}, {'mean': 28.74, 'sd': 6.920}, {'mean': 24.21, 'sd': 6.752}, {'mean': 20.50, 'sd': 5.504}, {'mean': 13.882, 'sd': 5.375}]
        elif age >= 41 or age <= 50:
            norms = [{'mean': 46.75, 'sd': 5.454}, {'mean': 35.57, 'sd': 6.391}, {'mean': 30.32, 'sd': 7.408}, {'mean': 30.04, 'sd': 7.790}, {'mean': 24.36, 'sd': 8.220}, {'mean': 17.250, 'sd': 7.866}]
        elif age >= 51 or age <= 60:
            norms = [{'mean': 50.12, 'sd': 4.983}, {'mean': 19.80, 'sd': 6.868}, {'mean': 18.48, 'sd': 6.482}, {'mean': 18.20, 'sd': 6.988}, {'mean': 15.44, 'sd': 6.494}, {'mean': 16.840, 'sd': 7.034}]
        elif age >= 61 or age <= 70:
            norms = [{'mean': 26.17, 'sd': 7.602}, {'mean': 19.33, 'sd': 6.358}, {'mean': 20.00, 'sd': 5.222}, {'mean': 18.00, 'sd': 6.755}, {'mean': 19.75, 'sd': 7.461}, {'mean': 16.583, 'sd': 3.423}]
        elif age >= 71 or age <= 80:
            norms = [{'mean': 29.44, 'sd': 8.900}, {'mean': 24.94, 'sd': 7.190}, {'mean': 22.22, 'sd': 6.358}, {'mean': 22.50, 'sd': 8.305}, {'mean': 20.22, 'sd': 8.882}, {'mean': 20.222, 'sd': 8.371}]
        else:
            norms = None
        return norms

    def get_simple_data(self, age):
        norms = None
        if age >= 18 or age <= 20:
            norms = [{'mean': 6.03, 'sd': 4.201}, {'mean': 11.68, 'sd': 5.978}, {'mean': 7.66, 'sd': 3.765}, {'mean': 6.21, 'sd': 2.338}, {'mean': 5.95, 'sd': 3.748}, {'mean': 5.61, 'sd': 3.201}]
        elif age >= 21 or age <= 30:
            norms = [{'mean': 17.66, 'sd': 8.845}, {'mean': 11.29, 'sd': 4.177}, {'mean': 8.09, 'sd': 4.680}, {'mean': 7.14, 'sd': 3.379}, {'mean': 6.31, 'sd': 2.958}, {'mean': 7.26, 'sd': 3.592}]
        elif age >= 31 or age <= 40:
            norms = [{'mean': 19.53, 'sd': 7.836}, {'mean': 13.00, 'sd': 5.774}, {'mean': 9.88, 'sd': 5.353}, {'mean': 7.74, 'sd': 4.515}, {'mean': 7.38, 'sd': 3.931}, {'mean': 6.65, 'sd': 3.256}]
        elif age >= 41 or age <= 50:
            norms = [{'mean': 20.25, 'sd': 6.162}, {'mean': 12.82, 'sd': 6.007}, {'mean': 11.25, 'sd': 5.841}, {'mean': 11.39, 'sd': 6.391}, {'mean': 8.00, 'sd': 3.672}, {'mean': 8.11, 'sd': 4.614}]
        elif age >= 51 or age <= 60:
            norms = [{'mean': 20.20, 'sd': 6.103}, {'mean': 14.04, 'sd': 6.072}, {'mean': 12.28, 'sd': 5.542}, {'mean': 10.48, 'sd': 5.924}, {'mean': 8.68, 'sd': 3.827}, {'mean': 9.2, 'sd': 3.979}]
        elif age >= 61 or age <= 70:
            norms = [{'mean': 20.42, 'sd': 7.428}, {'mean': 12.67, 'sd': 6.344}, {'mean': 14.50, 'sd': 6.068}, {'mean': 12.17, 'sd': 5.967}, {'mean': 11.08, 'sd': 5.485}, {'mean': 8.42, 'sd': 2.314}]
        elif age >= 71 or age <= 80:
            norms = [{'mean': 21.39, 'sd': 7.617}, {'mean': 14.44, 'sd': 6.051}, {'mean': 13.83, 'sd': 5.272}, {'mean': 13.17, 'sd': 5.491}, {'mean': 13.00, 'sd': 6.615}, {'mean': 13.33, 'sd': 4.994}]
        else:
            norms = None
        return norms
    
    def get_biased_data(self):
        return {'simple': {'min': 0, 'max':19.89, 'mean': 7.9782, 'sd': 4.67605}, 'total': {'min': 56.00, 'max':274.00, 'mean': 142.5800, 'sd': 52.50932}}
    '''
    def get_simple_distance_data(self, age):
        
    '''

class Trial(models.Model):
    test = models.ForeignKey(NvmtTest, related_name='trial', on_delete=models.CASCADE)
    trial_num = models.IntegerField(default=1)

    class Meta:
        unique_together = ('test', 'trial_num')
        ordering = ['trial_num']


class Card(models.Model):
    card_num = models.IntegerField(default=1)
    trial = models.ForeignKey(Trial, related_name='card', on_delete=models.CASCADE)

class Target(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    card = models.ForeignKey(Card, related_name='targets', on_delete=models.CASCADE)
    is_goal = models.BooleanField(default=False)
    click_time = models.DurationField(blank=True)