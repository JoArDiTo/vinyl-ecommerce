from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Vinyl)
admin.site.register(Song)
admin.site.register(Category)
admin.site.register(VinylCategory)