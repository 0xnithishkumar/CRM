# Generated by Django 4.2.3 on 2023-07-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_db',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='customer_db',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
