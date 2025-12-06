from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # Using the string ID from frontend "arctic-parka"
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    display_price = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    description = models.TextField()
    features = models.JSONField(default=list)
    sizes = models.JSONField(default=list)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
