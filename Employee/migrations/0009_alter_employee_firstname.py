# Generated by Django 5.0.7 on 2024-07-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0008_alter_employee_email_alter_employee_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='firstname',
            field=models.TextField(),
        ),
    ]
