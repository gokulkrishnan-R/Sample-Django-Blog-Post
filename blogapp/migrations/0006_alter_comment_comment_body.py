# Generated by Django 4.1.1 on 2022-11-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_comment_posted_on_alter_posts_posted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_body',
            field=models.CharField(max_length=120),
        ),
    ]
