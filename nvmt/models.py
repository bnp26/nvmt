from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    tester = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    def get_full_name(self):
        return self.first_name + ' ' + first.last_name

    def get_username(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

class Subject(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    HIGH_SCHOOL = 'HS'
    ACCOCIATE = 'A'
    BACHELORS = 'B'
    MASTERS = 'MS'
    DOCTORAL = 'MD'
    PHD = 'P'
    EDU_CHOICES = (
        (HIGH_SCHOOL, 'High School'),
        (ACCOCIATE, 'Associate Degree'),
        (BACHELORS, 'Bachelors Degree'),
        (MASTERS, 'Masters'),
        (DOCTORAL, 'Doctor of Medicin'),
        (PHD, 'PhD'),
    )

    age = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=OTHER)
    education = models.CharField(max_length=2, choices=EDU_CHOICES, default=HIGH_SCHOOL)

class Test(models.Model):
    user = models.ManyToManyField(User)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

class Trial(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    trial_num = models.IntegerField(default=1)

class Card(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    finish = models.DateTimeField()
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE)

class Point(models.Model):
    x_val = models.IntegerField(default=0)
    y_val = models.IntegerField(default=0)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    is_target = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True)
    clicked_at = models.DateTimeField(blank=True)
    click_time = models.DurationField(blank=True)
