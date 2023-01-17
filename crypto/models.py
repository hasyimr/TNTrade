from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Wallet(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    money = models.FloatField(null=True)

    def __str__(self):
        return str(self.user)


class CryptoWallet(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    bitcoin = models.FloatField(null=True, default=0)
    ethereum = models.FloatField(null=True, default=0)
    tether = models.FloatField(null=True, default=0)
    usdcoin = models.FloatField(null=True, default=0)
    binancecoin = models.FloatField(null=True, default=0)
    binanceusd = models.FloatField(null=True, default=0)
    ripple = models.FloatField(null=True, default=0)
    cardano = models.FloatField(null=True, default=0)
    dogecoin = models.FloatField(null=True, default=0)
    solana = models.FloatField(null=True, default=0)

    def __str__(self):
        return str(self.user)


class Coins(models.Model):
    coins = models.CharField(max_length=50)

    def __str__(self):
        return str(self.coins)


class InvestmentPrice(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    bitcoin = models.FloatField(null=True, default=0)
    ethereum = models.FloatField(null=True, default=0)
    tether = models.FloatField(null=True, default=0)
    usdcoin = models.FloatField(null=True, default=0)
    binancecoin = models.FloatField(null=True, default=0)
    binanceusd = models.FloatField(null=True, default=0)
    ripple = models.FloatField(null=True, default=0)
    cardano = models.FloatField(null=True, default=0)
    dogecoin = models.FloatField(null=True, default=0)
    solana = models.FloatField(null=True, default=0)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
        CryptoWallet.objects.create(user=instance)
        InvestmentPrice.objects.create(user=instance)
