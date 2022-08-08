# Generated by Django 4.0.6 on 2022-08-08 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee_name', models.CharField(max_length=80)),
                ('assignee_pic_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee_name', models.CharField(max_length=80)),
                ('assignee_pic_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=80)),
                ('expiration_date', models.DateField()),
                ('expiration_time', models.TimeField()),
                ('action_text', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('assignees', models.ManyToManyField(to='todo.assignee')),
                ('listed_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('resources', models.ManyToManyField(to='todo.resources')),
            ],
        ),
    ]
