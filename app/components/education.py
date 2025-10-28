import reflex as rx


def education_section() -> rx.Component:
    """Renders the education section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Education",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4",
            ),
            rx.el.div(class_name="h-1 w-20 bg-orange-500 mx-auto mb-12"),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("school", class_name="h-10 w-10 text-orange-500"),
                        class_name="p-4 bg-orange-100 rounded-lg inline-block",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Master of Business Administration (MBA)",
                            class_name="text-xl font-bold text-gray-800",
                        ),
                        rx.el.p(
                            "University of Information Technology and Management, Rzeszów",
                            class_name="text-orange-600 font-semibold",
                        ),
                        rx.el.p(
                            "Sep 2019 - Oct 2020", class_name="text-gray-500 text-sm"
                        ),
                        class_name="flex-1",
                    ),
                    class_name="flex items-center gap-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "graduation-cap", class_name="h-10 w-10 text-orange-500"
                        ),
                        class_name="p-4 bg-orange-100 rounded-lg inline-block",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "B.E, Electronics and Communication",
                            class_name="text-xl font-bold text-gray-800",
                        ),
                        rx.el.p(
                            "Anna University, Chennai, Tamil Nadu",
                            class_name="text-orange-600 font-semibold",
                        ),
                        rx.el.p(
                            "Sep 2002 - Jul 2006", class_name="text-gray-500 text-sm"
                        ),
                        class_name="flex-1",
                    ),
                    class_name="flex items-center gap-6",
                ),
                class_name="max-w-3xl mx-auto space-y-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="education",
        class_name="py-20 md:py-28 bg-white",
    )