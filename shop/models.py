from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    CATEGORIES = (
        ('W', 'Weapons'),
        ('D', 'Dresses'),
        ('F', 'Furniture'),
        ('Fo', 'Food'),
    )
    category = models.CharField(max_length = 2, choices = CATEGORIES)

    def __str__(self):
        return self.name
