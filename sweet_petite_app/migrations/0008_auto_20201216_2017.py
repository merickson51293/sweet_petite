# Generated by Django 2.2 on 2020-12-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0007_auto_20201216_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
