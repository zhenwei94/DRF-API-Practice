# Generated by Django 3.1.2 on 2020-10-26 16:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(related_name='authors', to='api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Booknumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn10', models.IntegerField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
                ('isbn13', models.IntegerField(validators=[django.core.validators.MinLengthValidator(13), django.core.validators.MinLengthValidator(13)])),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='bookNumber',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.booknumber'),
        ),
    ]