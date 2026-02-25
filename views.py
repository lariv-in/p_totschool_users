from lariv.registry import ViewRegistry
from lariv.views import AppsPage


# @ViewRegistry.register("lariv.AppsPage")
class PatchedAppsPage(AppsPage):
    def prepare_data(self, request, **kwargs):
        data = super().prepare_data(request, **kwargs)
        apps_dict = data.get("apps", {})

        # Stop 'users' and 'preferences' apps from displaying for non-superusers
        if not (request.user.is_superuser or request.user.role in ["totschool_admin"]):
            apps_dict.pop("users", None)
            apps_dict.pop("preferences", None)

        data["apps"] = apps_dict
        return data
