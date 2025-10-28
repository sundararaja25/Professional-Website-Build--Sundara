import reflex as rx
from app.state import PortfolioState


def nav_item(item: rx.Var[dict], is_mobile: bool = False) -> rx.Component:
    """Renders a navigation item."""
    on_click_event = rx.cond(is_mobile, PortfolioState.toggle_mobile_menu, rx.noop())
    return rx.el.a(
        item["name"],
        href=item["href"],
        on_click=on_click_event,
        class_name="text-gray-600 hover:text-orange-500 transition-colors duration-200 font-medium text-lg md:text-base",
    )


def mobile_menu() -> rx.Component:
    """Renders the mobile hamburger menu and its content."""
    return rx.el.div(
        rx.el.button(
            rx.icon(
                tag=rx.cond(PortfolioState.is_mobile_menu_open, "x", "menu"),
                class_name="h-6 w-6 text-gray-800",
            ),
            on_click=PortfolioState.toggle_mobile_menu,
            class_name="p-2 rounded-md hover:bg-gray-100",
        ),
        rx.cond(
            PortfolioState.is_mobile_menu_open,
            rx.el.div(
                rx.foreach(
                    PortfolioState.nav_items,
                    lambda item: nav_item(item, is_mobile=True),
                ),
                class_name="absolute top-16 right-4 z-50 w-48 bg-white rounded-xl shadow-lg p-4 flex flex-col items-start space-y-4",
            ),
            None,
        ),
        class_name="md:hidden",
    )


def desktop_nav() -> rx.Component:
    """Renders the desktop navigation links."""
    return rx.el.nav(
        rx.foreach(PortfolioState.nav_items, nav_item),
        class_name="hidden md:flex items-center space-x-8",
    )


def navbar() -> rx.Component:
    """Renders the main navigation bar."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("file_code_2", class_name="h-8 w-8 text-orange-500"),
                rx.el.span(
                    "Sundara",
                    class_name="text-xl font-bold text-gray-800 tracking-tighter",
                ),
                class_name="flex items-center space-x-2",
            ),
            rx.el.div(desktop_nav(), mobile_menu(), class_name="flex items-center"),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center",
        ),
        class_name="sticky top-0 z-50 py-4 bg-white/80 backdrop-blur-md border-b border-gray-200",
    )