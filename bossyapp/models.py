from django.db import models

# Create your models here.
class Bossy(models.Model):
    input = models.CharField(max_length=250)

    def __str__(self):
        return self.input