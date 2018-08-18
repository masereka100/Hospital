from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Patient(models.Model):
    STATUS_CHOICE = (
        ('admitted','Admitted'),
        ('outpatient','OutPatient'),
    )
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    IdNumber = models.CharField(max_length=250)
    Disease = models.CharField(max_length=250)
    Prescription  = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.FirstName


