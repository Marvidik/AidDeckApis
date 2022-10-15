from django.contrib import admin
from .models import BankDetails, BankWallet, FundApply
# Register your models here.


admin.site.register(BankDetails)
admin.site.register(BankWallet)
admin.site.register(FundApply)