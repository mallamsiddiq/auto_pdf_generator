# Generated by Django 4.0.2 on 2022-02-22 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_document_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='api.transaction'),
        ),
    ]