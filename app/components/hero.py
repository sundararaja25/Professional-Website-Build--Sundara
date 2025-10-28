import reflex as rx
from app.state import PortfolioState


def hero_section() -> rx.Component:
    """Renders the hero section of the portfolio."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        PortfolioState.full_name,
                        class_name="text-4xl md:text-6xl font-extrabold text-gray-800 tracking-tighter",
                    ),
                    rx.el.h2(
                        PortfolioState.title,
                        class_name="text-2xl md:text-3xl font-semibold text-orange-500 mt-2",
                    ),
                    rx.el.p(
                        PortfolioState.tagline,
                        class_name="mt-4 text-lg text-gray-600 max-w-2xl",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                "View My Work",
                                rx.icon("arrow-down", class_name="ml-2 h-5 w-5"),
                                class_name="px-8 py-3 bg-orange-500 text-white font-semibold rounded-lg shadow-md hover:bg-orange-600 transition-all duration-200 transform hover:scale-105 flex items-center",
                            ),
                            href="#projects",
                        ),
                        rx.el.a(
                            rx.el.button(
                                "Download Resume",
                                rx.icon("download", class_name="ml-2 h-5 w-5"),
                                class_name="px-8 py-3 bg-white text-gray-700 font-semibold rounded-lg border border-gray-300 shadow-sm hover:bg-gray-50 hover:border-gray-400 transition-all duration-200 transform hover:scale-105 flex items-center",
                            ),
                            href=PortfolioState.resume_path,
                            download=True,
                        ),
                        class_name="mt-8 flex flex-col sm:flex-row gap-4",
                    ),
                    class_name="flex flex-col items-center md:items-start text-center md:text-left",
                ),
                rx.el.div(
                    rx.el.image(
                        src=PortfolioState.avatar_url,
                        alt=f"Avatar of {PortfolioState.full_name}",
                        class_name="w-64 h-64 md:w-80 md:h-80 rounded-full object-cover shadow-lg border-4 border-white",
                    ),
                    class_name="hidden md:block",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-32 grid md:grid-cols-2 gap-12 items-center",
            )
        ),
        id="home",
        class_name="bg-gray-50",
    )