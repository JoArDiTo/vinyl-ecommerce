from django.db import models
from app_users.models import User
from app_products.models import Vinyl
import random

class CreditCard(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=16)
    number = models.CharField(max_length=16, unique=True)
    expiration = models.CharField(max_length=5) # MM/YY
    cvv = models.CharField(max_length=3)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"creditCard{random.randint(100000, 999999)}"
        super(CreditCard, self).save(*args, **kwargs)
        
class Purchase(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=16)
    product = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"purchase{random.randint(10000000, 99999999)}"
        self.total = self.product.price * self.quantity
        super(Purchase, self).save(*args, **kwargs)