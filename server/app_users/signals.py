from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from .models import User
from app_checkout.models import CreditCard, Purchase
from django.apps import apps

@receiver(post_migrate, sender=apps.get_app_config('app_checkout'))
def create_client_group(sender, **kwargs):
    group_name = 'client'
    
    group, created = Group.objects.get_or_create(name=group_name)
    
    if created:
        models_and_permissions = {
            User: ['change_user', 'delete_user', 'view_user'],
            CreditCard: ['add_creditcard', 'change_creditcard', 'delete_creditcard', 'view_creditcard'],
            Purchase: ['add_purchase', 'change_purchase', 'delete_purchase', 'view_purchase'],          
        }
        
        for model, permissions in models_and_permissions.items():
            content_type = ContentType.objects.get_for_model(model)
            
            for perm in permissions:
                permission = Permission.objects.get(
                    codename=perm,
                    content_type=content_type,
                )
                group.permissions.add(permission)
        
        print(f'Added "{group_name}" group and assigned permissions.')
    else:
        print(f' "{group_name}" group already exists.')
