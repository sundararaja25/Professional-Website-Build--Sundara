import reflex as rx
from app.state import PortfolioState


def skill_card(category: rx.Var[dict]) -> rx.Component:
    """Renders a card for a skill category."""
    return rx.el.div(
        rx.el.div(
            rx.icon(category["icon"], class_name="h-8 w-8 text-orange-500"),
            rx.el.h3(category["name"], class_name="text-lg font-bold text-gray-800"),
            class_name="flex items-center gap-4 mb-4",
        ),
        rx.el.div(
            rx.foreach(
                category["skills"],
                lambda skill: rx.el.span(
                    skill,
                    class_name="bg-orange-100 text-orange-800 text-sm font-medium px-3 py-1 rounded-full",
                ),
            ),
            class_name="flex flex-wrap gap-2",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def skills_section() -> rx.Component:
    """Renders the skills section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Technical Skills",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4",
            ),
            rx.el.div(class_name="h-1 w-20 bg-orange-500 mx-auto mb-12"),
            rx.el.div(
                rx.foreach(PortfolioState.skills, skill_card),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="skills",
        class_name="py-20 md:py-28 bg-white",
    )