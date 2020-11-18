# Generated by Django 2.2.10 on 2020-11-18 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_auto_20201118_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='user',
        ),
        migrations.AddField(
            model_name='poll',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_polls', to=settings.AUTH_USER_MODEL),
        ),
    ]