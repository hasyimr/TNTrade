from django import forms
from django.core.exceptions import ValidationError
from .models import Wallet, Coins, CryptoWallet


class PurchaseForm(forms.Form):
    form = Coins.objects.all()
    coin = forms.ModelChoiceField(queryset=form)
    amount = forms.IntegerField(required=True, label='Beli Berapa Bang?')
