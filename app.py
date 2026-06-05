from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

skills_data = {
    "python": {
        "name": "Python",
        "icon": "fa-brands fa-python",
        "rating": 4,
        "description": "Python is my main programming language. I use it for backend development, automation, data handling, and building practical applications.",
        "learned": ["Core Python", "OOP concepts", "File handling", "Exception handling", "APIs", "Automation basics"],
        "projects": ["Portfolio backend", "Contact form with SQLite", "Web scraping practice", "Data analysis scripts"]
    },
    "django": {
        "name": "Django",
        "image": "images/django.jpg",
        "rating": 3,
        "description": "I use Django for building structured and secure backend applications with database support.",
        "learned": ["Models", "Views", "Templates", "Admin panel", "URL routing", "Database handling"],
        "projects": ["Dynamic web applications", "Backend practice projects"]
    },
    "flask": {
        "name": "Flask",
        "image": "images/flask_img.png",
        "rating": 4,
        "description": "Flask helps me create lightweight and flexible web applications using Python.",
        "learned": ["Routes", "Templates", "Forms", "SQLite integration", "Static files", "Jinja templates"],
        "projects": ["Personal portfolio", "Contact form system", "Mini web apps"]
    },
    "data-analytics": {
    "name": "Data Analytics",
    "icon": "fa-solid fa-chart-line",
    "rating": 3,
    "description": "I use data analytics concepts to understand datasets, find patterns, and create useful insights.",
    "learned": ["Data cleaning", "Data visualization", "Basic statistics", "Trend analysis"],
    "projects": ["Dataset analysis practice", "Charts and reports"]
    },
    "excel": {
        "name": "Excel",
        "image": "images/excel.svg",
        "rating": 3,
        "description": "I use Excel to organize data, perform calculations, create reports, and analyze information clearly.",
        "learned": ["Formulas", "Tables", "Charts", "Data cleaning", "Pivot tables"],
        "projects": ["Spreadsheet reports", "Data analysis practice", "Dashboard preparation"]
    },
    "power-bi": {
        "name": "Power BI",
        "image": "images/power-bi.svg",
        "rating": 3,
        "description": "I use Power BI to create interactive dashboards and turn raw data into meaningful business insights.",
        "learned": ["Dashboard design", "Data modeling", "Visual reports", "Filters", "DAX basics"],
        "projects": ["Business intelligence dashboards", "Data visualization practice"]
    },
    "tableau": {
        "name": "Tableau",
        "image": "images/tableau.svg",
        "rating": 3,
        "description": "I use Tableau to build clean visual analytics dashboards that make data easier to understand.",
        "learned": ["Charts", "Dashboards", "Filters", "Data connections", "Storytelling with data"],
        "projects": ["Visual analytics dashboards", "Data storytelling practice"]
    },
    "html": {
        "name": "HTML",
        "icon": "fa-brands fa-html5",
        "rating": 4,
        "description": "I use HTML to create clean and structured web pages.",
        "learned": ["Semantic tags", "Forms", "Tables", "Page structure", "Accessibility basics"],
        "projects": ["Portfolio pages", "Forms", "Landing sections"]
    },
    "css": {
        "name": "CSS",
        "icon": "fa-brands fa-css3",
        "rating": 4,
        "description": "I use CSS to design responsive, attractive, and modern user interfaces.",
        "learned": ["Flexbox", "Grid", "Animations", "Responsive design", "Hover effects"],
        "projects": ["Portfolio UI", "Galaxy background", "Responsive sections"]
    },
    "bootstrap": {
        "name": "Bootstrap",
        "icon": "fa-brands fa-bootstrap",
        "rating": 3,
        "description": "Bootstrap helps me build responsive layouts quickly.",
        "learned": ["Grid system", "Buttons", "Cards", "Navbar", "Responsive utilities"],
        "projects": ["Responsive web layouts", "UI practice pages"]
    },
    "sql": {
        "name": "SQL",
        "icon": "fa-solid fa-database",
        "rating": 3,
        "description": "I use SQL for storing, querying, and managing application data.",
        "learned": ["Tables", "Insert", "Select", "Update", "Delete", "SQLite basics"],
        "projects": ["Portfolio contact database", "Database practice"]
    },
    "git": {
        "name": "Git",
        "icon": "fa-brands fa-git",
        "rating": 3,
        "description": "I use Git and GitHub for version control and managing my projects.",
        "learned": ["Commit", "Push", "Pull", "Branches", "GitHub repositories"],
        "projects": ["Portfolio version control", "Project management"]
    },
    "numpy": {
        "name": "NumPy",
        "icon": "fa-solid fa-cubes",
        "rating": 3,
        "description": "I use NumPy for numerical operations and working with arrays in Python.",
        "learned": ["Arrays", "Array operations", "Mathematical functions", "Data processing basics"],
        "projects": ["Numerical computing practice"]
    },
    "pandas": {
        "name": "Pandas",
        "icon": "fa-solid fa-grip",
        "rating": 3,
        "description": "I use Pandas for data cleaning, manipulation, and analysis.",
        "learned": ["DataFrames", "CSV handling", "Filtering", "Grouping", "Cleaning data"],
        "projects": ["Dataset analysis", "CSV data projects"]
    },
    "matplotlib": {
        "name": "Matplotlib",
        "icon": "fa-solid fa-chart-column",
        "rating": 3,
        "description": "I use Matplotlib to create charts and visual reports from data.",
        "learned": ["Line charts", "Bar charts", "Pie charts", "Graph styling"],
        "projects": ["Data visualization reports", "Chart practice"]
    }
}

projects_data = {
    "django-polls": {
        "title": "Django Polls App",
        "image": "images/jango.jpg",
        "source": "https://github.com/devendranikam1004/Django_Project/tree/main/Polls%20App",
        "description": "A Django-based polls application built with Python, HTML, CSS, and database integration. The project includes dynamic voting, question management, and user interaction features.",
        "tech_stack": ["Python", "Django", "HTML", "CSS", "SQLite/MySQL"],
        "features": ["Dynamic poll questions", "Voting system", "Database-driven content", "Responsive frontend", "User interaction flow"],
        "learned": ["Django routing", "Models and database handling", "Template rendering", "Form handling", "Backend logic"],
        "gallery": [
            {
                "image": "images/polls_home.png",
                "caption": "Project home page where users can see available polls."
            },
            {
                "image": "images/vote.png",
                "caption": "Voting page where users select an option and submit their vote."
            },
            {
                "image": "images/final_show.png",
                "caption": "Result page showing vote count and poll outcome."
            }
        ]
    },
    "portfolio-site": {
        "title": "Professional Portfolio Site",
        "image": "images/flask.jpg",
        "source": "https://github.com/devendranikam1004/Devendra_Portfolio",
        "description": "A responsive portfolio website developed using Flask, Python, HTML and  CSS to showcase projects, skills, resume, and contact information professionally.",
        "tech_stack": ["Python", "Flask", "HTML", "CSS", "SQLite"],
        "features": ["Animated hero section", "Contact form", "Skills carousel", "Project showcase", "Responsive layout"],
        "learned": ["Flask routes", "Jinja templates", "Canvas background", "Form handling", "Portfolio structure"],
        "gallery": [
            {
                "image": "images/P1.png",
                "caption": "Animated portfolio home page with star background."
            },
            {
                "image": "images/P2.png",
                "caption": "Skills carousel and interactive skill detail pages."
            }
        ]
    },
    "web-scraping": {
        "title": "Web Scraping",
        "image": "images/wbs.png",
        "source": "https://github.com/devendranikam1004/Dev_web_scraping_project/blob/master/AmbitionBox.ipynb",
        "description": "A Python web scraping project for collecting Company information such as Name, rating, salaries, service, interviews.",
        "tech_stack": ["Python", "BeautifulSoup", "Requests", "Data Cleaning"],
        "features": ["Automated data extraction", "Product information collection", "Structured output", "Reusable scraping logic"],
        "learned": ["HTML parsing", "HTTP requests", "Data extraction", "Cleaning scraped data", "Automation basics"],
        "gallery": [
            {
                "image": "images/W1.png",
                "caption": "Scraped data output collected from the website."
            },
            {
                "image": "images/W2.png",
                "caption": "Python scraping workflow using Requests and BeautifulSoup."
            }
        ]
    },
    "bookstore-website": {
        "title": "Bookstore-ecommerce-django",
        "image": "images/B1.png",
        "source": "https://github.com/devendranikam1004/BooksStore_website_using_Django",
        "description": "A bookstore website project designed to present books, categories, pricing, and browsing flows in a clean web interface.",
        "tech_stack": ["Python", "Flask/Django", "HTML", "CSS", "SQLite"],
        "features": ["Book listing pages", "Category-based browsing", "Book detail view", "Responsive layout", "Database-ready structure"],
        "learned": ["Catalog page design", "Template reuse", "Content organization", "Responsive card layouts", "Backend-driven pages"],
        "gallery": [
            {
                "image": "images/B1.png",
                "caption": "Bookstore website interface focused on clean browsing and product presentation."
            },
             {
                "image": "images/B2.png",
                "caption": "Bookstore website interface focused on clean browsing and product presentation."
            }
        ]
    },
    "library-management": {
        "title": "Library Management System",
        "image": "images/lb.png",
        "source": "https://github.com/devendranikam1004",
        "description": "A library management system project for handling books, members, issue records, returns, and organized library operations.",
        "tech_stack": ["Python", "Django/Flask", "HTML", "CSS", "SQLite"],
        "features": ["Book record management", "Member management", "Issue and return workflow", "Search-friendly structure", "Admin-focused interface"],
        "learned": ["CRUD operations", "Relational data handling", "Form validation", "Admin workflow planning", "Database-backed dashboards"],
        "gallery": [
            {
                "image": "images/lm1.png",
                "caption": "Management-style interface for organizing library records and daily operations."
            },
            {
                "image": "images/lm2.png",
                "caption": "Management-style interface for organizing library records and daily operations."
            }
        ]
    },
    "role-authentication": {
        "title": "Role Based Authentication System",
        "image": "images/rba.jpg",
        "source": "https://github.com/devendranikam1004",
        "description": "A role based authentication system built to manage secure login flows and separate access for users, admins, and protected pages.",
        "tech_stack": ["Python", "Flask/Django", "HTML", "CSS", "SQLite", "Authentication"],
        "features": ["User login and logout", "Role-based page access", "Protected routes", "Session handling", "Admin and user separation"],
        "learned": ["Authentication logic", "Authorization checks", "Session-based workflows", "Secure route protection", "User role modeling"],
        "gallery": [
            {
                "image": "images/flask_img.png",
                "caption": "Authentication project preview showing the backend framework focus."
            }
        ]
    }
}


def save_contact_message():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = sqlite3.connect("portfolio.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)

    cur.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        save_contact_message()

        return redirect("/")

    return render_template(
        "index.html",
        projects=projects_data,
        page_title="Devendra Nikam | Python Developer Portfolio",
        meta_description="Portfolio of Devendra Nikam, an aspiring Python developer skilled in Flask, Django, data analysis, web scraping, and responsive web applications."
    )


@app.route("/about")
def about_page():
    return render_template(
        "about-page.html",
        page_title="About Devendra Nikam | Python Developer",
        meta_description="Learn about Devendra Nikam's background in Statistics, Python development, Flask, Django, data analysis, and full-stack web projects."
    )


@app.route("/<section_name>", methods=["GET", "POST"])
def section_page(section_name):
    sections = {
        "skills": "skills",
        "projects": "work",
        "education": "education",
        "contact": "contact"
    }

    if section_name == "home":
        return redirect("/")

    if section_name not in sections:
        return redirect("/")

    if request.method == "POST":
        save_contact_message()
        return redirect(request.path)

    section_titles = {
        "skills": "Skills | Devendra Nikam Portfolio",
        "projects": "Projects | Devendra Nikam Portfolio",
        "education": "Education | Devendra Nikam Portfolio",
        "contact": "Contact Devendra Nikam | Python Developer"
    }

    section_descriptions = {
        "skills": "Explore Devendra Nikam's technical skills in Python, Flask, Django, SQL, data analytics, and frontend development.",
        "projects": "View Devendra Nikam's recent projects including Django apps, Flask portfolio work, web scraping, bookstore, library, and authentication systems.",
        "education": "Education details for Devendra Nikam, including Statistics academic background and technical learning foundation.",
        "contact": "Contact Devendra Nikam for Python development, Flask, Django, data analysis, and web application opportunities."
    }

    return render_template(
        "index.html",
        scroll_target=sections[section_name],
        projects=projects_data,
        page_title=section_titles[section_name],
        meta_description=section_descriptions[section_name]
    )


@app.route("/skill/<skill_name>")
def skill_page(skill_name):
    skill = skills_data.get(skill_name)

    if not skill:
        return redirect("/skills")

    return render_template(
        "skill-detail.html",
        skill=skill,
        page_title=f"{skill['name']} Skill | Devendra Nikam",
        meta_description=f"Details about Devendra Nikam's {skill['name']} skills, learning areas, and related project practice."
    )


@app.route("/project/<project_name>")
def project_page(project_name):
    project = projects_data.get(project_name)

    if not project:
        return redirect("/projects")

    return render_template(
        "project-detail.html",
        project=project,
        page_title=f"{project['title']} | Devendra Nikam Project",
        meta_description=project["description"]
    )


if __name__ == "__main__":
    app.run(debug=True)
