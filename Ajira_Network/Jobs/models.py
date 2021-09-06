from django.db import models

# Create your models here.


class Job(models.Model):
    position_name = models.CharField(max_length=100)
    text_description = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    salary= models.IntegerField()
    n_openings = models.IntegerField()
    