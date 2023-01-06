from django.db import models

# Create your models here.
class Product(models.Model):
    drop_down=[('kg','KG'),('mtr','Mtr'),('ltr','Ltr')]
    productImage=models.ImageField(upload_to="productapp/images")
    productName=models.CharField(max_length=200)
    price=models.IntegerField()
    unit=models.CharField(choices=drop_down, max_length=200)

    def __str__(self):
        return self.productName