# Generated by Django 3.2.9 on 2022-02-23 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoItems',
            new_name='TodoItem',
        ),
    ]
