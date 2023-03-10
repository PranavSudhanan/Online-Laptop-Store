# Generated by Django 4.1.5 on 2023-01-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0003_cartmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('fname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('paymode', models.CharField(choices=[('Debit/Credit Card', 'Debit/Credit Card'), ('Upi', 'Upi'), ('Cash on delivery', 'Cash on delivery')], max_length=25)),
            ],
        ),
    ]
