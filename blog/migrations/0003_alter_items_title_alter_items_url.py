# Generated by Django 4.0.1 on 2022-02-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_items_options_items_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='items',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
