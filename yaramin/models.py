from django.db import models

# Create your models here.

class items(models.Model):
    nameItem = models.CharField(max_length=50)

class itemDetails(models.Model):
    color = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    tax = models.FloatField()
    image = models.CharField(max_length=150)
    total = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    itemID = models.ForeignKey(items,on_delete=models.CASCADE, null=True)

