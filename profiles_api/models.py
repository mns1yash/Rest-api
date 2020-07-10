from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Mnaager for User Profiles"""

    def create_user(self, email, name, password=None):
        """ Create a new user Profile"""
        if not email:
            raise ValueError('User Must have an Email Address')

        email = self.normalize_email(email)
        #User model
        user = self.model(email= email, name=name)

        user.set_password(password)
        user.save(using= self._db)

        return user
    def create_superuser(self, email, name, password):
        """Creat and Save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        # We dint specify is super user anywhere because it automatically creates by PermissionsMixin

        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Data base Model for Users in tht System / Doc String"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    """ Model Manager"""
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieve Full Name of User"""
        return self.name


    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name

    def __str__self(self):
        """Return Represetation of our User """
        return self.email
