# Generated by Django 3.0.6 on 2020-05-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWeb', '0011_auto_20200521_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='title',
            field=models.CharField(default='Сайтын Тохиргоо', editable=False, max_length=250),
        ),
    ]
