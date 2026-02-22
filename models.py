from django.db.models.signals import post_migrate


def create_default_roles(sender, **kwargs):
    from users.models import Role

    Role.objects.get_or_create(name="totschool_student")
    Role.objects.get_or_create(name="totschool_admin")


post_migrate.connect(create_default_roles)
