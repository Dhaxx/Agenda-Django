# Generated by Django 4.2.7 on 2023-12-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, default='Testezada'),
        ),
    ]