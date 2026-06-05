# Devendra Nikam Portfolio

A personal portfolio website built with Flask to showcase skills, education, projects, resume, and contact information.

## Features

- Responsive portfolio homepage
- About section and full about page
- Skills carousel with individual skill detail pages
- Recent works/project showcase
- Project detail pages with screenshots and source links
- Education section
- Contact form with SQLite message storage
- Resume links
- SEO meta descriptions and favicon

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite
- Font Awesome
- Slick Carousel

## Project Structure

```text
portfolio/
├── app.py
├── portfolio.db
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   ├── files/
│   ├── images/
│   └── js/
└── templates/
    ├── index.html
    ├── about.html
    ├── about-page.html
    ├── skills.html
    ├── skill-detail.html
    ├── projects.html
    ├── project-detail.html
    ├── education.html
    ├── contact.html
    └── navbar.html
```

## Installation

1. Clone or download the project.

2. Open the project folder:

```bash
cd portfolio
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run The Project

```bash
python app.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000/
```

## Main Pages

- `/` - Home page
- `/about` - Full about page
- `/skills` - Skills section
- `/projects` - Recent works section
- `/education` - Education section
- `/contact` - Contact section
- `/skill/<skill_name>` - Skill detail page
- `/project/<project_name>` - Project detail page

## Contact Form

The contact form stores messages in `portfolio.db` using SQLite. The database table is created automatically when a message is submitted.

## Author

Devendra Nikam

- GitHub: [devendranikam1004](https://github.com/devendranikam1004)
- LinkedIn: [Devendra Nikam](https://www.linkedin.com/in/devendra-nikam-b689b6322/)
