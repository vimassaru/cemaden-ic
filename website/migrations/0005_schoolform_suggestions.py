# Generated by Django 5.1 on 2024-11-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_userrole_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolform',
            name='suggestions',
            field=models.TextField(blank=True, null=True),
        ),
    ]