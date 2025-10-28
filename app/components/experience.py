import reflex as rx
from app.state import PortfolioState


def experience_card(experience: rx.Var[dict], index: rx.Var[int]) -> rx.Component:
    """Renders a card for a single work experience entry."""
    is_even = index % 2 == 0
    card_content = rx.el.div(
        rx.el.div(
            rx.el.image(
                src=experience["logo"],
                alt=f"{experience['company']} logo",
                class_name="h-10 w-10 object-contain",
            ),
            rx.el.div(
                rx.el.h3(
                    experience["role"], class_name="text-lg font-bold text-gray-800"
                ),
                rx.el.p(
                    f"{experience['company']} | {experience['dates']}",
                    class_name="text-orange-600 font-semibold text-sm",
                ),
                class_name="flex-1",
            ),
            class_name="flex items-center gap-4 mb-4",
        ),
        rx.el.ul(
            rx.foreach(
                experience["responsibilities"],
                lambda resp: rx.el.li(resp, class_name="text-gray-600 text-sm"),
            ),
            class_name="list-disc list-inside space-y-2",
        ),
        class_name="relative bg-white p-6 rounded-xl border border-gray-200 w-full md:w-[calc(50%-2rem)] hover:shadow-lg transition-shadow duration-300",
    )
    timeline_marker = rx.el.div(
        rx.el.div(
            class_name="h-4 w-4 bg-orange-500 rounded-full border-4 border-gray-50"
        ),
        class_name="absolute top-8 -translate-y-1/2 left-1/2 -translate-x-1/2",
    )
    return rx.el.div(
        rx.cond(is_even, card_content, rx.el.div(class_name="hidden md:block w-full")),
        rx.el.div(timeline_marker, class_name="relative hidden md:block w-16"),
        rx.cond(is_even, rx.el.div(class_name="hidden md:block w-full"), card_content),
        class_name="flex items-start w-full",
    )


def experience_section() -> rx.Component:
    """Renders the experience timeline section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Professional Experience",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4",
            ),
            rx.el.div(class_name="h-1 w-20 bg-orange-500 mx-auto mb-16"),
            rx.el.div(
                rx.el.div(
                    rx.foreach(PortfolioState.experience, experience_card),
                    class_name="flex flex-col items-center gap-8 md:gap-0",
                ),
                class_name="relative before:content-[''] before:absolute before:top-0 before:left-1/2 before:-translate-x-1/2 before:w-0.5 before:h-full before:bg-gray-200",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="experience",
        class_name="py-20 md:py-28 bg-gray-50",
    )