# Generated by Django 4.1.5 on 2023-01-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0009_alter_wallet_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptowallet',
            name='binancecoin',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='binanceusd',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='bitcoin',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='cardano',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='dogecoin',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='ethereum',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='solana',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='tether',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='usdcoin',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cryptowallet',
            name='xrp',
            field=models.FloatField(default=0, null=True),
        ),
    ]
