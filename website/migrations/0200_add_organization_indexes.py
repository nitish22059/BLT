# Generated by Django 5.1.6 on 2025-02-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0199_organization_slug"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="organization",
            index=models.Index(fields=["created"], name="org_created_idx"),
        ),
        migrations.AddIndex(
            model_name="domain",
            index=models.Index(fields=["organization"], name="domain_org_idx"),
        ),
        migrations.AddIndex(
            model_name="issue",
            index=models.Index(fields=["domain", "status"], name="issue_domain_status_idx"),
        ),
        migrations.AddIndex(
            model_name="ip",
            index=models.Index(fields=["path", "created"], name="ip_path_created_idx"),
        ),
        migrations.AddIndex(
            model_name="project",
            index=models.Index(fields=["organization"], name="project_org_idx"),
        ),
        migrations.AddIndex(
            model_name="repo",
            index=models.Index(fields=["project"], name="repo_project_idx"),
        ),
    ]
