# Generated by Django 3.1.4 on 2020-12-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_emailcollector_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcollector',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
