# Generated by Django 3.2.9 on 2022-03-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_delete_todoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='photos',
            field=models.ImageField(default='no_image', upload_to='images'),
            preserve_default=False,
        ),
    ]
