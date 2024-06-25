from django.db import models
import random

class Vinyl(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=16)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=250)
    price = models.FloatField(default=0.00)
    year = models.IntegerField()
    country = models.CharField(max_length=60)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=255, default="images/default-vinyl-photo.webp")
    release_date = models.DateTimeField(auto_now_add=True)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"vinyl{random.randint(1000000, 9999999)}"
        super(Vinyl, self).save(*args, **kwargs)
        

class Song(models.Model):
    id= models.CharField(primary_key=True, editable=False, max_length=16)
    title = models.CharField(max_length=80)
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"song{random.randint(10000000, 99999999)}"
        super(Song, self).save(*args, **kwargs)
        
class Category(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=16)
    name = models.CharField(max_length=80)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"category{random.randint(100000, 999999)}"
        super(Category, self).save(*args, **kwargs)
        
class VinylCategory(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=20)
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"vinylCategory{random.randint(10000, 99999)}"
        super(VinylCategory, self).save(*args, **kwargs)