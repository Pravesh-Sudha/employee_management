from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
