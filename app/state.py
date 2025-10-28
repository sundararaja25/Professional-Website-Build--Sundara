import reflex as rx
from typing import TypedDict, Optional
import re
import asyncio


class NavItem(TypedDict):
    name: str
    href: str


class Experience(TypedDict):
    logo: str
    company: str
    role: str
    dates: str
    responsibilities: list[str]


class SkillCategory(TypedDict):
    name: str
    icon: str
    skills: list[str]


class Project(TypedDict):
    image: str
    title: str
    description: str
    technologies: list[str]
    github_url: str
    demo_url: str


class PortfolioState(rx.State):
    """Manages the state for the portfolio website."""

    nav_items: list[NavItem] = [
        {"name": "Home", "href": "#home"},
        {"name": "About", "href": "#about"},
        {"name": "Experience", "href": "#experience"},
        {"name": "Skills", "href": "#skills"},
        {"name": "Projects", "href": "#projects"},
        {"name": "Education", "href": "#education"},
        {"name": "Contact", "href": "#contact"},
    ]
    is_mobile_menu_open: bool = False
    full_name: str = "Sundara Raja Perumal"
    title: str = "AI Strategy Consultant & Digital Transformation Leader"
    tagline: str = "Driving enterprise-wide digital transformation through strategic AI implementation and cloud-native innovation."
    resume_path: str = "/Sundara_Raja_Perumal_Resume (1).pdf"
    avatar_url: str = f"https://api.dicebear.com/9.x/notionists/svg?seed=AI%20Strategy&backgroundColor=ff8c00,f5f5f5&backgroundType=gradientLinear"
    professional_summary: str = "Seasoned AI Strategy Consultant and Digital Transformation Leader with over a decade of experience advising global enterprises. I specialize in crafting and executing AI-driven strategies that unlock new revenue streams, optimize operations, and create sustainable competitive advantages. My work has delivered over $50M in transformation value by integrating cutting-edge GenAI solutions with robust cloud-native architectures. As an MBA-qualified advisor, I excel at bridging the gap between executive vision and technical implementation, ensuring that innovation translates to measurable business impact."
    specializations: list[dict[str, str]] = [
        {
            "icon": "brain-circuit",
            "title": "AI Strategy & Implementation",
            "desc": "Crafting bespoke AI roadmaps and leading the implementation of GenAI solutions to solve complex business challenges.",
        },
        {
            "icon": "refresh-cw-dot",
            "title": "Digital Transformation Consulting",
            "desc": "Advising C-suite leaders on enterprise-wide transformation to enhance agility, efficiency, and market responsiveness.",
        },
        {
            "icon": "cloud-cog",
            "title": "Enterprise Architecture & Cloud Strategy",
            "desc": "Designing scalable, secure, and future-proof enterprise architectures on modern cloud platforms.",
        },
        {
            "icon": "lightbulb",
            "title": "Innovation & Change Management",
            "desc": "Fostering a culture of innovation and guiding organizations through the complexities of technological change.",
        },
    ]
    experience: list[Experience] = [
        {
            "logo": "/placeholder.svg",
            "company": "SkyBlueMedia, UAE",
            "role": "Chief Technology Officer",
            "dates": "Jun 2025 - Present",
            "responsibilities": [
                "Led digital transformation initiatives, increasing operational efficiency by 40%.",
                "Spearheaded AI and IoT adoption, resulting in 25% revenue growth.",
                "Established robust cybersecurity frameworks, reducing data breaches by 60%.",
                "Optimized DevOps pipelines, reducing time-to-market by 30%.",
            ],
        },
        {
            "logo": "/placeholder.svg",
            "company": "RescaleLab, Singapore",
            "role": "Chief Technical Advisor",
            "dates": "Nov 2023 - Jun 2025",
            "responsibilities": [
                "Pioneered GenAI-powered personalized learning platforms using LLMs.",
                "Achieved a 40% increase in learning efficiency and user engagement.",
                "Led platform scalability to support user base growth of over 50%.",
                "Optimized software architecture, reducing system downtime by 30%.",
            ],
        },
        {
            "logo": "/placeholder.svg",
            "company": "Innov8, Chennai",
            "role": "Chief Information Officer",
            "dates": "Oct 2019 - Nov 2023",
            "responsibilities": [
                "Defined and executed IT strategy aligned with business goals, managing a $5M budget.",
                "Led Salesforce CRM implementation, increasing user satisfaction by 30%.",
                "Ensured 99.9% uptime for critical systems through robust infrastructure.",
            ],
        },
        {
            "logo": "/htdc_logo.png",
            "company": "HTC Global Services, Chennai",
            "role": "Full Stack Lead",
            "dates": "Feb 2018 - Oct 2019",
            "responsibilities": [
                "Architected and led the development of microservices-based SaaS products.",
                "Improved team productivity by 20% through Agile practices.",
                "Reduced application deployment time by 40% with CI/CD automation.",
            ],
        },
        {
            "logo": "/tcs_logo.png",
            "company": "Cognizant, Chennai",
            "role": "Senior Software Engineer",
            "dates": "Jul 2013 - Feb 2018",
            "responsibilities": [
                "Led development of scalable, high-performance applications for enterprise clients.",
                "Optimized database queries and application logic, improving system performance by 25%.",
                "Mentored and trained junior engineers, fostering technical growth.",
            ],
        },
        {
            "logo": "/alten_logo.png",
            "company": "ALTEN, Chennai",
            "role": "Module Lead",
            "dates": "Sep 2010 - Jul 2013",
            "responsibilities": [
                "Managed a 5-member team in design, development, and testing.",
                "Achieved a 15% reduction in delivery times through process optimization.",
                "Utilized Agile methodologies to streamline development processes.",
            ],
        },
    ]
    skills: list[SkillCategory] = [
        {
            "name": "Leadership & Strategy",
            "icon": "user-cog",
            "skills": [
                "Technology Leadership",
                "C-Level Management",
                "Tech Strategy",
                "Team Leadership",
                "Stakeholder Communication",
            ],
        },
        {
            "name": "Cloud & DevOps",
            "icon": "cloud-cog",
            "skills": [
                "AWS",
                "Azure",
                "Cloud-Native",
                "DevOps",
                "CI/CD",
                "Docker",
                "Kubernetes",
                "DevSecOps",
            ],
        },
        {
            "name": "AI & Data",
            "icon": "brain-circuit",
            "skills": [
                "GenAI",
                "LLMs",
                "Machine Learning",
                "AI Models",
                "Data Analytics",
            ],
        },
        {
            "name": "Frameworks & Architectures",
            "icon": "cuboid",
            "skills": ["Microservices", "Django", "Flask", "React", "Node.js"],
        },
        {
            "name": "Languages & Databases",
            "icon": "code-2",
            "skills": [
                "Python",
                "Java",
                "JavaScript",
                "MySQL",
                "PostgreSQL",
                "MongoDB",
            ],
        },
        {
            "name": "Certifications & Tools",
            "icon": "award",
            "skills": [
                "SAFe® 4 Practitioner",
                "Design Thinking",
                "Cloud AI Certified",
                "Git",
                "Jenkins",
                "Salesforce",
                "Agile/Scrum",
            ],
        },
    ]
    projects: list[Project] = [
        {
            "image": "/placeholder.svg",
            "title": "GenAI-Powered Learning Platform",
            "description": "Pioneered a personalized adaptive learning platform using Large Language Models (LLMs), resulting in a 40% increase in learning efficiency and user engagement.",
            "technologies": ["GenAI", "LLMs", "Python", "AI Models"],
            "github_url": "#",
            "demo_url": "#",
        },
        {
            "image": "/placeholder.svg",
            "title": "Cloud-Native Digital Transformation",
            "description": "Led an enterprise-wide initiative leveraging cloud-native architectures to drive a 40% increase in operational efficiency and 25% revenue growth.",
            "technologies": ["AWS", "Cloud-Native", "DevOps", "Microservices"],
            "github_url": "#",
            "demo_url": "",
        },
        {
            "image": "/placeholder.svg",
            "title": "Enterprise CRM Implementation",
            "description": "Directed the successful implementation of Salesforce CRM, integrating it across business units to increase user satisfaction by 30%.",
            "technologies": ["Salesforce", "IT Strategy", "Agile", "CI/CD"],
            "github_url": "",
            "demo_url": "#",
        },
    ]
    form_data: dict[str, str] = {}
    form_errors: dict[str, str] = {}
    is_submitting: bool = False

    @rx.event
    def toggle_mobile_menu(self):
        """Toggles the visibility of the mobile navigation menu."""
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    def _validate_form(self, form_data: dict[str, str]) -> bool:
        self.form_errors = {}
        if not form_data.get("name", "").strip():
            self.form_errors["name"] = "Name is required."
        if not form_data.get("email", "").strip():
            self.form_errors["email"] = "Email is required."
        elif not re.match("[^@]+@[^@]+\\.[^@]+", form_data["email"]):
            self.form_errors["email"] = "Invalid email address."
        if not form_data.get("subject", "").strip():
            self.form_errors["subject"] = "Subject is required."
        if not form_data.get("message", "").strip():
            self.form_errors["message"] = "Message is required."
        elif len(form_data["message"]) < 10:
            self.form_errors["message"] = "Message must be at least 10 characters."
        return not self.form_errors

    @rx.event
    async def handle_submit(self, form_data: dict[str, str]):
        self.is_submitting = True
        self.form_errors = {}
        yield
        if not self._validate_form(form_data):
            self.is_submitting = False
            yield rx.toast.error(
                "Please correct the errors in the form.", duration=3000
            )
            return
        self.form_data = form_data
        await asyncio.sleep(2)
        self.is_submitting = False
        yield rx.toast.success(
            "Your message has been sent successfully!", duration=3000
        )
        self.form_data = {}
        self.form_errors = {}

    @rx.var
    def current_year(self) -> int:
        from datetime import datetime

        return datetime.now().year