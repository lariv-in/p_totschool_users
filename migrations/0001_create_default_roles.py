from django.db import migrations


def create_default_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    Role.objects.get_or_create(name="totschool_student")
    Role.objects.get_or_create(name="totschool_admin")


def delete_default_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    Role.objects.filter(name__in=["totschool_student", "totschool_admin"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_role"),
    ]

    operations = [
        migrations.RunPython(create_default_roles, delete_default_roles),
    ]
