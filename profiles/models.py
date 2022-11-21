from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
    BaseUserManager)
from django.core.mail import send_mail


class UserProfileManager(BaseUserManager):
    '''userprofile manager'''

    def create_user(self, email, password, first_name, **extra_fields):
        '''create and save a new user'''
        if email is None:
            raise ValueError("Email field is required!")
        if first_name is None or len(first_name) == 0:
            raise ValueError('First name field is required!')
        email = self.normalize_email(email)

        user = self.model(email=email, password=password,
                          first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, **extra_fields):
        '''create and save a new super user'''
        superuser = self.create_user(
            email, password, first_name, **extra_fields)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Database model for users in the system'''
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

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


class FeedModel(models.Model):
    '''defines the model for a feed resource'''
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feeds'
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''returns a string representation of the FeedModel'''
        return self.status_text
