from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from .models import User
from django.apps import apps

@receiver(post_migrate, sender=apps.get_app_config('app_users'))
def create_client_group(sender, **kwargs):
    group_name = 'client'
    
    group, created = Group.objects.get_or_create(name=group_name)
    
    if created:
        models_and_permissions = {
            User: ['view_user', 'change_user', 'delete_user'],
            # permissions for products and checkout to implement            
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
