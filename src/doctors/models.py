from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    reg_date = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    qualifications = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    sub_speciality = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name