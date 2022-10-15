from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Missionary(models.Model):
    # for missionaries
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    moi=models.ImageField(upload_to="IDS")
    denomenational_affliation=models.CharField(max_length=100)

    # for missionaries guarsntor
    Gname=models.CharField(max_length=100)
    Gemail=models.EmailField()
    Gphone_number=models.IntegerField()
    Gaddress=models.CharField(max_length=100)
    Gnationality=models.CharField(max_length=100)
    Gmoi=models.ImageField(upload_to="IDS")
    Gdenomenational_affliation=models.CharField(max_length=100)


class BankDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bank_name=models.CharField(max_length=100)
    account_num=models.IntegerField()
    account_name=models.CharField(max_length=100)

class BankWallet(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    amount=models.IntegerField()


class FundApply(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
    amount=models.IntegerField()
    images=models.ImageField(upload_to="location_images")
    date=models.DateTimeField()

