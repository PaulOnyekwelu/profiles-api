from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
    BaseUserManager)
from django.core.mail import send_mail


class UserProfileManager(BaseUserManager):
    '''contains userprofile management functions'''
    pass


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Database model for users in the system'''
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        '''return string representation of userprofile model'''
        return self.email

    def get_full_name(self):
        '''return the first and last name with a space in-btw'''
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        '''return the user first name'''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
