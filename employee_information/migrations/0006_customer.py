# Generated by Django 4.2.4 on 2023-08-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0005_auto_20220302_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('locationid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
