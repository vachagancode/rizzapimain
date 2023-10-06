from django.db import models

# Create your models here.
class Rizz(models.Model):
    rizz = models.CharField(max_length=455)

    def __str__(self):
        return self.rizz