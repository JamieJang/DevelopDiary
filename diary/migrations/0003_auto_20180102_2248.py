# Generated by Django 2.0 on 2018-01-02 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20171227_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-id']},
        ),
    ]
