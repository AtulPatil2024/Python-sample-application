# Generated by Django 5.0.7 on 2024-07-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_alter_employee_email_alter_employee_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='firstname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lastname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
