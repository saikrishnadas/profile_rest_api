# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("Enter a vaild Email")

        user = self.models(email=self.normalize_email(email),name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,name,email,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(max_length =255 , unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
