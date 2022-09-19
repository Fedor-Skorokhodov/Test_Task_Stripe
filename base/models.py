from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
