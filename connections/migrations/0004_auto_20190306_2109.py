# Generated by Django 2.1.5 on 2019-03-06 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_auto_20190306_2050'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together=set(),
        ),
    ]
