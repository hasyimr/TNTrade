from django.contrib import admin

# Register your models here.
from .models import Wallet, CryptoWallet, Coins, InvestmentPrice


admin.site.register(Wallet)
admin.site.register(CryptoWallet)
admin.site.register(Coins)
admin.site.register(InvestmentPrice)
