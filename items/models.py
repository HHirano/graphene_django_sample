from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return self.name
