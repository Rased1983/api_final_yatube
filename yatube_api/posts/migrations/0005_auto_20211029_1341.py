# Generated by Django 2.2.16 on 2021-10-29 10:41

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211029_1336'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='%(app_label)s_%(class)s_prevent_self_follow',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('following')), name='%(app_label)s_%(class)s_not_self_follow'),
        ),
    ]
