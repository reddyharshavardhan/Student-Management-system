from django.db import models
from django.contrib.auth.models import User
#import pickle
import datetime
import os
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join("uploads/",filename)


class Group(models.Model):
    slug = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)


    def __str__(self):
        return self.name

class Branch(models.Model):
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)
    Reg = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    student_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    gender = models.CharField(max_length=100, null=False, blank=False)
    mobile = models.CharField(max_length=10)
    dob = models.DateField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Fail, 1-Pass")
    subjects = models.ManyToManyField('Subject')
    Batch = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name


class Subject(models.Model):
    Code = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    credits = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name