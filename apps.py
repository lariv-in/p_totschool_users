from django.apps import AppConfig
from lariv.registry import MetaRegistry


class TotschoolUsersConfig(AppConfig):
    name = "p_totschool_users"

    def ready(self):
        from . import ui, views  # noqa: F401

        UsersMeta = MetaRegistry.get("users")

        @MetaRegistry.register("users")
        class NewUsersMeta(UsersMeta):
            roles = ["totschool_admin"]


@MetaRegistry.register("p_totschool_users")
class TotschoolUsersMeta:
    p_type = "plugin"
    verbose_name = "Totschool Users"
    url_prefix = "totschool_users"
