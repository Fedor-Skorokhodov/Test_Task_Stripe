from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Discount(models.Model):
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return str(self.rate) + '%'


class Tax(models.Model):
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return str(self.rate) + '%'


class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    session_key = models.CharField(max_length=50, unique=True)
    items = models.ManyToManyField(Item, related_name='items', blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.DO_NOTHING, null=True, blank=True)