# Generated by Django 4.1.7 on 2023-03-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(blank=True, null=True, to='study.lesson', verbose_name='Уроки'),
        ),
    ]