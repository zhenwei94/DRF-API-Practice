# Generated by Django 3.1.2 on 2020-11-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201105_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='api.Book'),
        ),
    ]
