# Generated by Django 4.0.5 on 2022-07-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0003_alter_course_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
