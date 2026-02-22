from lariv.registry import UIRegistry, ComponentRegistry


def add_hello_message(c):
    # Insert the message before the apps grid
    c.children.insert(
        0,
        ComponentRegistry.get("column")(
            uid="apps-top-column",
            children=[
                ComponentRegistry.get("row")(
                    uid="apps-hello-row",
                    classes="flex items-end gap-2 text-3xl font-bold text-base-content mb-2 mt-4 max-w-5xl mx-auto px-6",
                    children=[
                        ComponentRegistry.get("text_field")(
                            uid="apps-hello-text",
                            static_value="Hello, ",
                        ),
                        ComponentRegistry.get("text_field")(
                            uid="apps-hello-name",
                            key="request.user.name",
                        ),
                    ],
                ),
            ],
        ),
    )
    return c


# Patch the AppsPage to include the dynamic Hello message
UIRegistry.get("lariv.AppsPage").patch(
    uid="apps-scaffold",
    fn=add_hello_message,
)
