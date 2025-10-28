import reflex as rx
from app.state import PortfolioState


def footer() -> rx.Component:
    """Renders the footer of the website."""
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                f"© {PortfolioState.current_year} {PortfolioState.full_name}. All Rights Reserved.",
                class_name="text-sm text-gray-500",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("github", class_name="h-6 w-6"),
                    href="https://github.com",
                    target="_blank",
                    class_name="text-gray-400 hover:text-orange-500 transition-colors",
                ),
                rx.el.a(
                    rx.icon("linkedin", class_name="h-6 w-6"),
                    href="https://linkedin.com",
                    target="_blank",
                    class_name="text-gray-400 hover:text-orange-500 transition-colors",
                ),
                class_name="flex items-center space-x-4",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center",
        ),
        class_name="py-8 bg-white border-t border-gray-200",
    )