# Generated by Django 3.1.4 on 2020-12-15 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_emailcollector_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcollector',
            name='salary',
            field=models.FloatField(default=1, max_length=20, verbose_name='Salary'),
            preserve_default=False,
        ),
    ]