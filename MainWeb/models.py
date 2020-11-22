from django.db import models
from datetime import datetime

class General_University(models.Model):
    uid=models.IntegerField(primary_key=True)
    uName=models.CharField(max_length=1000)
    location=models.CharField(max_length=50)
    website=models.CharField(max_length=250)
    def __str__(self):
        return self.uName

class General_University_requirement(models.Model):

    universityid=models.ForeignKey(
    'General_University',on_delete=models.CASCADE
    )
    requireGpa=models.DecimalField(max_digits=5, decimal_places=2)
    unit=models.CharField(max_length=1)
    background=models.CharField(max_length=50)
    passingyear=models.IntegerField(default=2019)
    examdate=models.DateField(default=datetime.now)


class Medical_College(models.Model):
    uId=models.IntegerField(primary_key=True)
    uName=models.CharField(max_length=500)
    requireGpa=models.DecimalField(max_digits=5, decimal_places=2)
    passingyear=models.IntegerField(default=2019)
    location=models.CharField(max_length=250)
    website=models.CharField(max_length=250)
    biology=models.DecimalField(max_digits=5, decimal_places=2)
    english=models.DecimalField(max_digits=5, decimal_places=2)
    examdate=models.DateField(default=datetime.now)

    def __str__(self):
        return self.uName


class Science_And_Technology(models.Model):
    universityid=models.IntegerField(primary_key=True)
    uName=models.CharField(max_length=500)
    location=models.CharField(max_length=50)
    website=models.CharField(max_length=250)

    def __str__(self):
        return self.uName


class Science_And_Technology_requirement(models.Model):

    uId=models.ForeignKey(
    'Science_And_Technology',on_delete=models.CASCADE
    )
    unit=models.CharField(max_length=1)
    requireGpa=models.DecimalField(max_digits=5, decimal_places=2)
    background=models.CharField(max_length=50)
    passingyear=models.IntegerField(default=2019)
    examdate=models.DateField(default=datetime.now)

class Engineering_University(models.Model):

    uId=models.IntegerField(primary_key=True)
    uName=models.CharField(max_length=500)
    requireGpa=models.DecimalField(max_digits=5, decimal_places=2)
    background=models.CharField(max_length=50)
    passingyear=models.IntegerField(default=2019)
    English=models.DecimalField(max_digits=5, decimal_places=2)
    pyhsics=models.DecimalField(max_digits=5, decimal_places=2)
    chemistry=models.DecimalField(max_digits=5, decimal_places=2)
    math=models.DecimalField(max_digits=5, decimal_places=2)
    location=models.CharField(max_length=50)
    website=models.CharField(max_length=250)
    examdate=models.DateField(default=datetime.now)

    def __str__(self):
        return self.uName
