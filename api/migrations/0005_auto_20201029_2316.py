# Generated by Django 3.1.2 on 2020-10-29 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.book'),
        ),
    ]