# Google Developer Groups Web Platform

AyyappaSwamy121/Google-Developer-Groups

## Overview

This project is a web platform for Google Developer Groups (GDG), facilitating community events, networking, and learning resources for developers. It features event management, galleries, quizzes, and certificate issuance for participants.

## Features

- **Event Listings & Details:** Browse and participate in GDG events.
- **Gallery:** Visual showcase of GDG activities and events.
- **Contact & About Pages:** Info about the team and contact options.
- **Authentication:** User registration and login with responsive design.
- **Quizzes:** Take quizzes on various tech topics (Android, Firebase, Flutter, Gemini, Kotlin, Kaggle, etc.).
- **Score Tracking:** View scores for completed quizzes.
- **Certificate Generation:** Automatically generate and download certificates upon quiz completion.
- **Modern UI:** Sections like "AI Revolution" featuring Google Gemini 2.0.
- **Responsive Design:** Works on mobile and desktop.
- **Admin Utilities:** JavaScript helpers for formatting and core logic.

## Quiz & Certificate Workflow

- After login, users can choose from multiple courses/topics and take quizzes.
- Quizzes are dynamically loaded per topic, scored, and results saved.
- On successful quiz completion, users can download a personalized certificate (generated using Python's PIL library) with their name rendered on a template.

## Technologies Used

- **Backend:** Django 5.0.1 (Python)
- **Frontend:** HTML, CSS (Poppins font), JavaScript (jQuery, Owl Carousel)
- **Templates:** Django template system
- **Static Files:** Under `/static/` and `/GDG/static/`
- **Certificate Generation:** Python PIL (Pillow)
- **License:** MIT License (for some assets)

## Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/AyyappaSwamy121/Google-Developer-Groups.git
   ```
2. **Install dependencies**
   - Make sure Python 3.10+ and Django 5.0.1 are installed.
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```
3. **Run the Django server**
   ```bash
   python manage.py runserver
   ```
4. **Access the platform**
   - Go to `http://localhost:8000/`
   - Register/login, take quizzes, and download certificates.

## Project Structure

- `GDG/`: Main app for templates, static files, quiz/certificate logic.
- `PECGDG/settings.py`: Django settings and config.
- `productionfiles/`, `staticfiles/`, `static/`: Static resources and admin assets.

## Contributors

- Designed and developed by the ALR Team
- Example team member: Ganeshula veera Ramana ([LinkedIn](https://www.linkedin.com/in/gveeravenkataramana/), [Email](mailto:ramanavasu9th@gmail.com))

## License

MIT License (see [static/admin/img/LICENSE](static/admin/img/LICENSE) and [productionfiles/admin/img/LICENSE](productionfiles/admin/img/LICENSE))

## Acknowledgments

- Google Developer Groups Community
- Django documentation
- Themeforest for UI inspiration

---
© 2025 Designed and Developed by ALR Team