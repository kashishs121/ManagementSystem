from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from . import managers
# from django.contrib.auth import user
# from django.contrib.auth.models import User


# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)

class Users(AbstractBaseUser):
    USER = 'user'
    STAFF = 'staff'
    role_choice=(
        ('USER','user'),
       ('STAFF_USER','staff_user')
    )
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=role_choice,default=USER)
    is_superuser = models.BooleanField(blank=True,null=True)
    USERNAME_FIELD = 'username'
    objects = managers.UserManager()
# Create your models here.

# class user(models.Model):
#     name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     password1 = models.CharField(max_length=100)
class BookHotel(models.Model):
    name = models.CharField(max_length=200)
    booking_location = models.CharField(max_length=200)
    available_from = models.DateField()
    available = models.DateField()
    def __str__(self) -> str:
        return self.name

class BookSpecificHotel(models.Model):
    bookHotel = models.ForeignKey('BookHotel', on_delete=models.CASCADE)
    bookno = models.CharField(max_length=200)
    available_from = models.DateField()
    available = models.DateField()
    booked = models.DateField(null=True, blank=True)
    is_booked = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.bookno