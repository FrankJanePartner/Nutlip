from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    USER_TYPE_CHOICES = (
        ('agent', 'Agent'),
        ('buyer', 'Buyer'),
        ('conveyancer', 'Conveyancer'),
        ('broker', 'Broker'),  # Fix the typo here
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
    # Add unique related_name for groups
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    # Add unique related_name for user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
