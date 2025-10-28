import reflex as rx
from app.state import PortfolioState
from app.components.navbar import navbar
from app.components.hero import hero_section
from app.components.about import about_section
from app.components.experience import experience_section
from app.components.skills import skills_section
from app.components.projects import projects_section
from app.components.education import education_section
from app.components.contact import contact_section
from app.components.footer import footer


def index() -> rx.Component:
    """The main portfolio page."""
    return rx.el.main(
        navbar(),
        hero_section(),
        about_section(),
        experience_section(),
        skills_section(),
        projects_section(),
        education_section(),
        contact_section(),
        footer(),
        class_name="font-['Open_Sans'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap",
            rel="stylesheet",
        ),
        rx.el.style("""
            /* Add smooth scrolling behavior */
            html {
                scroll-behavior: smooth;
            }
            """),
    ],
)
app.add_page(index, title="Sundara Raja Perumal | Senior Software Engineer")