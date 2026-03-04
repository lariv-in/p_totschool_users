from django.apps import AppConfig
from lariv.registry import ConfigRegistry


@ConfigRegistry.register("p_totschool_users")
class TotschoolUsersConfig(AppConfig):
    name = "p_totschool_users"
    p_type = "plugin"
    verbose_name = "Users"
    url_prefix = "users"
    icon = "user"

    def ready(self):
        # Patch the core users app to be visible to totschool_admin
        try:
            core_users_class = ConfigRegistry.get("users")
            core_users_class.roles = getattr(core_users_class, "roles", []) + [
                "totschool_admin"
            ]
        except ValueError:
            pass  # Core users app not registered

        from . import ui, views  # noqa: F401
