# Generated by Django 4.1.5 on 2023-01-15 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('crypto', '0011_rename_xrp_cryptowallet_ripple'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentPrice',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bitcoin', models.FloatField(default=0, null=True)),
                ('ethereum', models.FloatField(default=0, null=True)),
                ('tether', models.FloatField(default=0, null=True)),
                ('usdcoin', models.FloatField(default=0, null=True)),
                ('binancecoin', models.FloatField(default=0, null=True)),
                ('binanceusd', models.FloatField(default=0, null=True)),
                ('ripple', models.FloatField(default=0, null=True)),
                ('cardano', models.FloatField(default=0, null=True)),
                ('dogecoin', models.FloatField(default=0, null=True)),
                ('solana', models.FloatField(default=0, null=True)),
            ],
        ),
    ]