from django.contrib.auth.models import User
from django.db import models

import os
from binascii import hexlify, unhexlify

def _createId():
    new_id = hexlify(os.urandom(8)).decode('ASCII')
    print(new_id)
    return new_id

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

ETHNIC_CHOICES = (
    ('AfA', 'African American'),
    ('CA', 'Caucasian American'),
    ('AsA', 'Asian American'),
    ('HA', 'Hispanic American'),
    ('ArA', 'Arab American'),
    ('NA', 'Native American'),
)

EDU_CHOICES = (
    ('HS_WO/D', 'Some High School (No Diploma)'),
    ('HS_W/D', 'High School Diploma'),
    ('C_WO/D', 'Some College Experience (No Diploma)'),
    ('C_BA', 'Bachelor of Arts'),
    ('C_BS', 'Bachelor of Science'),
    ('C_MS', 'Master\'s Degree'),
    ('C_DO', 'Doctorate Degree'),
)

class Medication(models.Model):
    name = models.CharField(max_length = 80, blank=False)
    dosage = models.CharField(max_length = 5, blank=False)

    def __str__(self):
        return "{0} {1}".format(self.name, self.dosage)

class MedicalDiagnosis(models.Model):
    name = models.CharField(max_length = 120, blank=False)

    def __str__(self):
        return "{0}".format(self.name)
    
class PsychDiagnosis(models.Model):
    name = models.CharField(max_length = 120, blank=False)
    
    def __str__(self):
        return "{0}".format(self.name)

class Subject(models.Model):
    id = models.CharField(max_length=16, primary_key=True, default=_createId)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
    ethnicity = models.CharField(max_length = 3, choices=ETHNIC_CHOICES) 
    edu_lvl = models.CharField(max_length=9, choices=EDU_CHOICES)
    chronic_desc = models.CharField(max_length=155, blank=True, null=True)
    meds = models.ManyToManyField(Medication, blank=True)
    med_issues = models.ManyToManyField(MedicalDiagnosis, blank=True)
    mental_issues = models.ManyToManyField(PsychDiagnosis, blank=True)
    
    class Meta:
        ordering = ('created', 'id', )

class Test(models.Model):
    test_code = models.CharField(max_length=8, primary_key=True)
    test_type = models.CharField(max_length=45, default="PNMT", blank=False)
    subject = models.ForeignKey(Subject, related_name='test', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=12, default="Distributed")
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']