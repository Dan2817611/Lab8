# Generated by Django 4.2.7 on 2023-11-17 10:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='group',
        ),
        migrations.AlterField(
            model_name='reader',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reader',
            name='course',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='reader',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
