# Generated by Django 4.2.2 on 2023-06-20 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_remove_comment_likes_remove_comment_unlikes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
