# Generated by Django 5.1.8 on 2025-05-12

import os
import shutil

from django.conf import settings
from django.core.files import File
from django.db import migrations


def add_first_forum_post_badge_icon(apps, schema_editor):
    Badge = apps.get_model("website", "Badge")
    badge_title = "First Forum Post"
    icon_relative_path = "badges/icons8-forum-96.png"

    badge = Badge.objects.filter(title=badge_title).first()
    if badge:
        static_icon_path = os.path.join("website", "static", "img", icon_relative_path)

        if os.path.exists(static_icon_path):
            media_icon_path = os.path.join(settings.MEDIA_ROOT, "badges", os.path.basename(static_icon_path))
            os.makedirs(os.path.dirname(media_icon_path), exist_ok=True)
            shutil.copy(static_icon_path, media_icon_path)

            with open(media_icon_path, "rb") as f:
                badge.icon.save(os.path.basename(media_icon_path), File(f), save=True)
                badge.save()


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0239_remove_first_suggestion_badge"),
    ]

    operations = [
        migrations.RunPython(add_first_forum_post_badge_icon),
    ]
