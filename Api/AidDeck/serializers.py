from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from AidDeck.models import BankDetails,BankWallet,FundApply,Missionary



class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankDetails
        fields=["user","bank_name","account_num","account_name"]


class BankWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankWallet
        fields=["user","amount"]


class FundApplySerializer(serializers.ModelSerializer):
    class Meta:
        model=FundApply
        fields=["user","title","discription","amount","images"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]


class MissionarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Missionary
        fields=["user","phone_number","address","nationality","moi","denomenational_affliation","Gname","Gemail","Gphone_number","Gaddress","Gnationality","Gmoi","Gdenomenational_affliation"]
