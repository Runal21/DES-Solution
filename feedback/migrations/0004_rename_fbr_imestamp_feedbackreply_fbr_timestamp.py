# Generated by Django 5.0.4 on 2024-04-10 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_rename_fb_admin_feedbackreply_fbr_admin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackreply',
            old_name='fbr_imestamp',
            new_name='fbr_timestamp',
        ),
    ]