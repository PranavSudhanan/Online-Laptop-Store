# Generated by Django 4.1.5 on 2023-01-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0005_alter_cartmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='paymode',
            field=models.CharField(choices=[('Debit/Credit Card', 'Debit/Credit Card'), ('Upi', 'Upi'), ('Cash on delivery', 'Cash on delivery')], max_length=50),
        ),
    ]
