import reflex as rx
from app.state import PortfolioState


def project_card(project: rx.Var[dict]) -> rx.Component:
    """Renders a card for a single project."""
    return rx.el.div(
        rx.el.image(
            src=project["image"],
            alt=project["title"],
            class_name="rounded-t-xl object-cover h-48 w-full",
        ),
        rx.el.div(
            rx.el.h3(
                project["title"], class_name="text-lg font-bold text-gray-800 mb-2"
            ),
            rx.el.p(project["description"], class_name="text-gray-600 text-sm mb-4"),
            rx.el.div(
                rx.foreach(
                    project["technologies"],
                    lambda tech: rx.el.span(
                        tech,
                        class_name="bg-orange-100 text-orange-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                    ),
                ),
                class_name="flex flex-wrap gap-2 mb-4",
            ),
            rx.el.div(
                rx.cond(
                    project["github_url"] != "",
                    rx.el.a(
                        rx.icon("github", class_name="h-5 w-5 mr-2"),
                        "GitHub",
                        href=project["github_url"],
                        target="_blank",
                        class_name="flex items-center text-gray-600 hover:text-orange-500 font-semibold transition-colors",
                    ),
                    None,
                ),
                rx.cond(
                    project["demo_url"] != "",
                    rx.el.a(
                        rx.icon("external-link", class_name="h-5 w-5 mr-2"),
                        "Demo",
                        href=project["demo_url"],
                        target="_blank",
                        class_name="flex items-center text-gray-600 hover:text-orange-500 font-semibold transition-colors",
                    ),
                    None,
                ),
                class_name="flex items-center space-x-4 mt-auto pt-4 border-t border-gray-100",
            ),
            class_name="p-6 flex flex-col h-full",
        ),
        class_name="bg-white rounded-xl border border-gray-200 overflow-hidden flex flex-col hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def projects_section() -> rx.Component:
    """Renders the projects section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "My Projects",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4",
            ),
            rx.el.div(class_name="h-1 w-20 bg-orange-500 mx-auto mb-12"),
            rx.el.div(
                rx.foreach(PortfolioState.projects, project_card),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="projects",
        class_name="py-20 md:py-28 bg-gray-50",
    )