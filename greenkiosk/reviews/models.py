from django.db import models

# Create your models here.
from django.db import models


class Review(models.Model):
    product_name = models.CharField(max_length=32, default='')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.pk}"

