# Generated by Django 4.1.6 on 2023-02-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_api', '0002_alter_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]