# 🌱 PlantWise  
### AI-Based Plant Disease Detection System & Blog Platform

PlantWise is a **Django-powered web application** designed to help plant enthusiasts, farmers, and gardeners **identify plant diseases**, **learn plant care**, and **share knowledge through blogs** — all in one platform.

This project is built with **scalability and future AI integration** in mind.

---

## 🚀 Current Features

### 🔐 User Authentication
- User registration & login
- Secure authentication system
- Profile-based access control

### 📝 Blog System
- Create, edit, and delete blog posts
- Clean and structured content management
- Organized templates and static files

### 🏠 Core Pages
- Homepage and core navigation
- Modular app-based architecture

---

<<<<<<< HEAD
## 🧠 Planned AI Features (Upcoming)

PlantWise is being actively developed to include **AI-powered plant disease detection**:

- 🌿 Upload plant leaf images
- 🤖 Deep Learning model for disease classification
- 📊 Confidence score & disease explanation
- 💡 Suggested treatments & prevention tips
- 📈 Dataset expansion and model improvement

> The AI module will be integrated as a separate, scalable service to ensure performance and maintainability.
=======
## Plant Disease Diagnosis

- Upload plant leaf images
- Disease detection via KindWise API
- Confidence score for predictions
- Disease description and treatment suggestions
- Diagnosis history per user
>>>>>>> f0764ea (final commit)

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite (development)
- **Authentication:** Django Auth System
- **Version Control:** Git & GitHub

## Project Sturcture 
PlantWise/
│
├── accounts/ # User authentication & profiles
├── blog/ # Blog system
├── core/ # Core pages and shared logic
├── plantwise/ # Project settings & configuration
├── templates/ # Global templates
├── manage.py
└── .gitignore
---

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nafis-Kamal-CodeQuest/PlantWise---AI-based-plant-disease-detection-system-and-blog-website.git
cd PlantWise---AI-based-plant-disease-detection-system-and-blog-website
```
## Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Run Migrations
python manage.py migrate

## Start Deployment Server
python manage.py runserver

