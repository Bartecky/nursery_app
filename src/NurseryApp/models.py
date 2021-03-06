from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

CHILD_STATUS = (
    ('1', 'Verification'),
    ('2', 'Waiting'),
    ('3', 'Accepted')
)

CHILD_SEX = (
    ('1', 'M'),
    ('2', 'F')
)


# Create your models here.
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=9, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    day_of_birth = models.DateField()
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.CASCADE)
    activity = models.ManyToManyField('Activity', blank=True)
    diet = models.ManyToManyField('Diet', blank=True)
    registration_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=CHILD_STATUS, default='1')
    active = models.BooleanField(default=True)
    sex = models.CharField(max_length=1, choices=CHILD_SEX)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse_lazy('child-detail-view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'children'
        ordering = ['last_name']


class Group(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=9, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Caregiver(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=9, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    relationship_with_child = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse_lazy('caregiver-detail-view', kwargs={'pk': self.pk})


class Activity(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('activity-detail-view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Activities'


class Diet(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('diet-detail-view', kwargs={'pk': self.pk})


class Message(models.Model):
    sender = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Parent, on_delete=models.CASCADE)
    subject = models.CharField(max_length=256)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy('teacher-list-view')
