from django.apps import AppConfig


class TotschoolUsersConfig(AppConfig):
    name = "p_totschool_users"
    p_type = "plugin"
    verbose_name = "Users"
    url_prefix = "users"
    icon = "user"

    def ready(self):
        pass
