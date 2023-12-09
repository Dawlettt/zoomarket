from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone, location, password):
        if not username:
            raise ValueError('username bos bolmawi kerek')
        if not phone:
            raise ValueError('telefon nomer bos bolmawi kerek')
        if not password:
            raise ValueError('password bos bolmawi kerek')
        user = self.model(username=username, phone=phone, location=location)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, location, password):
        if not phone:
            raise ValueError("email bos bolmawi kerek")
        if not password:
            raise ValueError("password bos bolmawi kerek")
        user = self.create_user(username, phone, location, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    location = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'location']

    def __str__(self):
        return self.username
