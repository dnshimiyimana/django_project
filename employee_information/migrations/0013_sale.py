# Generated by Django 4.2.4 on 2023-09-09 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0012_alter_cdrlog_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100)),
                ('sale_date', models.DateField()),
                ('amount', models.IntegerField()),
                ('status', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.customer')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employees')),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.plan')),
            ],
        ),
    ]
