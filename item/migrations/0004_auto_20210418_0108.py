# Generated by Django 3.1.7 on 2021-04-17 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20210418_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name_plural': 'ระบบจ่ายเงิน'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='Itemid',
        ),
    ]
