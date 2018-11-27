from django.db import models

# Create your models here.
class Receipt(models.Model):
    item = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)

