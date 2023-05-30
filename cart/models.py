from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class Cart(models.Model):

    client = models.CharField(max_length=120, default='Anonymous')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)




    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


    def __str__(self):
        return f'Cart #:{self.id}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    line_total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

    def save(self, *args, **kwargs):
        self.line_total = self.product.price * self.quantity
        
        super(CartItem, self).save(*args, **kwargs)