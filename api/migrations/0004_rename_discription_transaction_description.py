# Generated by Django 4.0.2 on 2022-02-20 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_discripton_transaction_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='discription',
            new_name='description',
        ),
    ]
