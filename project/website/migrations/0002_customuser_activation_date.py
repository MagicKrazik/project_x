# Generated by Django 5.1 on 2024-09-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
