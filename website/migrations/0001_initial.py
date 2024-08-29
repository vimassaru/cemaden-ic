# Generated by Django 5.1 on 2024-08-26 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entity_code', models.CharField(max_length=10)),
                ('school_name', models.CharField(max_length=255)),
                ('uf_code', models.CharField(max_length=2)),
                ('uf', models.CharField(max_length=2)),
                ('town_code', models.CharField(max_length=10)),
                ('town_name', models.CharField(max_length=255)),
            ],
        ),
    ]
