# Generated by Django 2.2 on 2020-12-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0024_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
