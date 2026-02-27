from lariv.registry import UIRegistry
from components import *  # noqa

# Get the original AppsPage from the registry (do not import from file)
AppsPage = UIRegistry.get("lariv.AppsPage")


@UIRegistry.register("lariv.AppsPage")
class TotschoolAppsPage(AppsPage):
    def build(self):
        tree = super().build()
        tree.insert_before(
            "apps-grid",
            Column(
                uid="apps-top-column",
                children=[
                    Row(
                        uid="apps-hello-row",
                        classes="flex items-end gap-2 text-3xl font-bold text-base-content mb-2 mt-4 max-w-5xl mx-auto px-6",
                        children=[
                            TextField(
                                uid="apps-hello-text",
                                static_value="Hello, ",
                            ),
                            TextField(
                                uid="apps-hello-name",
                                key="request.user.name",
                            ),
                        ],
                    ),
                ],
            ),
        )
        return tree
