# Generated by Django 2.2.10 on 2020-11-24 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0015_auto_20201120_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_questions', to='polls.CompletedPoll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_question', to='polls.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='textanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChoiceAnswer',
        ),
        migrations.DeleteModel(
            name='MultiChoiceAnswer',
        ),
        migrations.DeleteModel(
            name='TextAnswer',
        ),
        migrations.AddField(
            model_name='completedpoll',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_polls', to='polls.Poll'),
        ),
        migrations.AddField(
            model_name='completedpoll',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_polls', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='completed_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.CompletedQuestion'),
        ),
    ]
