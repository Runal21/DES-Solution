# Generated by Django 5.0.4 on 2024-04-13 06:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumpost', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_title', models.CharField(max_length=200)),
                ('fp_content', models.TextField()),
                ('fp_created_at', models.DateTimeField(auto_now_add=True)),
                ('fp_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmfp_content', models.TextField()),
                ('cmfp_created_at', models.DateTimeField(auto_now_add=True)),
                ('cmfp_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumpost.forumpost')),
            ],
        ),
        migrations.DeleteModel(
            name='ForumPost_Create',
        ),
    ]
