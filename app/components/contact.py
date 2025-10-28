import reflex as rx
from app.state import PortfolioState


def contact_info_card(
    icon: str, title: str, content: str, href: str = ""
) -> rx.Component:
    """Renders a card for a piece of contact information."""
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-orange-500"),
            rx.el.h3(title, class_name="text-md font-semibold text-gray-800"),
            rx.el.p(content, class_name="text-sm text-gray-600"),
            class_name="flex flex-col items-center text-center space-y-2",
        ),
        href=href,
        class_name="bg-white p-6 rounded-xl border border-gray-200 hover:shadow-md hover:-translate-y-1 transition-all duration-300 w-full",
    )


def form_input(
    label: str, name: str, placeholder: str, type: str = "text"
) -> rx.Component:
    """A reusable form input component."""
    return rx.el.div(
        rx.el.label(
            label,
            htmlFor=name,
            class_name="block text-sm font-medium text-gray-700 mb-1",
        ),
        rx.el.input(
            type=type,
            name=name,
            id=name,
            placeholder=placeholder,
            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-orange-500 focus:border-orange-500",
        ),
        rx.cond(
            PortfolioState.form_errors.contains(name),
            rx.el.p(
                PortfolioState.form_errors[name], class_name="text-red-500 text-xs mt-1"
            ),
            None,
        ),
    )


def form_textarea(label: str, name: str, placeholder: str) -> rx.Component:
    """A reusable form textarea component."""
    return rx.el.div(
        rx.el.label(
            label,
            htmlFor=name,
            class_name="block text-sm font-medium text-gray-700 mb-1",
        ),
        rx.el.textarea(
            name=name,
            id=name,
            placeholder=placeholder,
            rows=4,
            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-orange-500 focus:border-orange-500",
        ),
        rx.cond(
            PortfolioState.form_errors.contains(name),
            rx.el.p(
                PortfolioState.form_errors[name], class_name="text-red-500 text-xs mt-1"
            ),
            None,
        ),
    )


def contact_section() -> rx.Component:
    """Renders the contact section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Get In Touch",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4",
            ),
            rx.el.div(class_name="h-1 w-20 bg-orange-500 mx-auto mb-12"),
            rx.el.div(
                contact_info_card(
                    "mail",
                    "Email",
                    "sundarinnov8@gmail.com",
                    href="mailto:sundarinnov8@gmail.com",
                ),
                contact_info_card(
                    "phone", "Phone", "+91 9585557084", href="tel:+919585557084"
                ),
                contact_info_card("map-pin", "Location", "Chennai, Tamil Nadu, India"),
                class_name="grid sm:grid-cols-3 gap-8 mb-16",
            ),
            rx.el.form(
                rx.el.div(
                    form_input("Full Name", "name", "John Doe"),
                    form_input(
                        "Email Address", "email", "john.doe@example.com", type="email"
                    ),
                    class_name="grid sm:grid-cols-2 gap-6",
                ),
                form_input("Subject", "subject", "Regarding a job opportunity..."),
                form_textarea("Message", "message", "Your message here..."),
                rx.el.button(
                    rx.cond(
                        PortfolioState.is_submitting,
                        rx.fragment(
                            rx.spinner(class_name="h-5 w-5 mr-3"), "Sending..."
                        ),
                        "Send Message",
                    ),
                    type="submit",
                    disabled=PortfolioState.is_submitting,
                    class_name="w-full flex justify-center py-3 px-4 bg-orange-500 text-white font-semibold rounded-lg shadow-md hover:bg-orange-600 transition-all duration-200 disabled:bg-orange-300",
                ),
                on_submit=PortfolioState.handle_submit,
                class_name="max-w-3xl mx-auto space-y-6",
                reset_on_submit=True,
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="contact",
        class_name="py-20 md:py-28 bg-gray-50",
    )