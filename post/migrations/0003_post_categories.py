# Generated by Django 2.0.7 on 2018-07-07 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.Category'),
        ),
    ]
