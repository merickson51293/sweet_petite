# Generated by Django 2.2 on 2020-12-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0014_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='picture',
            field=models.ImageField(default='Picture.jpg', upload_to='imgs/'),
            preserve_default=False,
        ),
    ]
