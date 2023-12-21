# Generated by Django 5.0 on 2023-12-21 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='level',
            field=models.IntegerField(
                choices=[
                    (0, 'First Level'),
                    (1, 'Second Level'),
                    (2, 'Third Level'),
                    (3, 'Fourth Level'),
                    (4, 'Fifth Level'),
                ],
                default=0,
            ),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('house_no', models.CharField(max_length=150)),
                (
                    'providers',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='contacts',
                        to='provider.provider',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('first_date_of_release', models.DateField(blank=True, null=True)),
                (
                    'providers',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='products',
                        to='provider.provider',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]