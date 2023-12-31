
from django.db import models
from django.utils import timezone

class Entry(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)



