import reflex as rx
from app.state import PortfolioState


def specialization_card(spec: rx.Var[dict]) -> rx.Component:
    """Renders a card for a specialization."""
    return rx.el.div(
        rx.el.div(
            rx.icon(spec["icon"], class_name="h-8 w-8 text-orange-500"),
            class_name="p-4 bg-orange-100 rounded-lg inline-block mb-4",
        ),
        rx.el.h3(spec["title"], class_name="text-lg font-bold text-gray-800 mb-2"),
        rx.el.p(spec["desc"], class_name="text-gray-600 text-sm"),
        class_name="bg-white p-6 rounded-xl border border-gray-200 hover:shadow-md hover:-translate-y-1 transition-all duration-300",
    )


def about_section() -> rx.Component:
    """Renders the about section of the portfolio."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "About Me",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4",
            ),
            rx.el.div(class_name="h-1 w-20 bg-orange-500 mx-auto mb-12"),
            rx.el.div(
                rx.el.div(
                    rx.el.image(
                        src="/placeholder.svg",
                        alt="Professional Headshot",
                        class_name="rounded-xl object-cover w-full h-full shadow-lg",
                    ),
                    class_name="w-full md:w-1/3",
                ),
                rx.el.div(
                    rx.el.p(
                        PortfolioState.professional_summary,
                        class_name="text-gray-600 text-lg mb-6 leading-relaxed",
                    ),
                    rx.el.div(
                        "10+ Years of Experience",
                        class_name="inline-block bg-orange-100 text-orange-700 font-semibold px-4 py-2 rounded-lg mb-8",
                    ),
                    rx.el.h3(
                        "My Specializations",
                        class_name="text-2xl font-bold text-gray-800 mb-6",
                    ),
                    rx.el.div(
                        rx.foreach(PortfolioState.specializations, specialization_card),
                        class_name="grid sm:grid-cols-2 gap-6",
                    ),
                    class_name="w-full md:w-2/3",
                ),
                class_name="flex flex-col md:flex-row gap-12 md:gap-16 items-start",
            ),
        ),
        id="about",
        class_name="py-20 md:py-28 bg-white",
    )