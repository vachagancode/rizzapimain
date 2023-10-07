from django.db import models

# Create your models here.
class Senetence(models.Model):
    senetence = models.CharField(max_length=655)

    def __str__(self):
        return self.senetence