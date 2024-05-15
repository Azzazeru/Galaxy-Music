from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

