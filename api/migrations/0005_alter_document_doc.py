# Generated by Django 4.0.2 on 2022-02-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_discription_transaction_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc',
            field=models.FileField(upload_to='transsaction_files'),
        ),
    ]