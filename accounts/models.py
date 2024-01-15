from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from .constants import ACCOUNT_TYPE, GENDER

class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateTimeField(null = True, blank = True)
    gender = models.CharField(max_length=20, choices=GENDER)
    initial_deposit_date = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=12)

    def __str__(self) -> str:
        return str(self.account_no)


class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name = 'address', on_delete = models.CASCADE )
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length = 100)
    
