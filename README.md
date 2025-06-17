Suvrudhi: Government Schemes Voice Bot
Suvrudhi is a multilingual web-based Interactive Voice Response (IVR) system designed to help rural Indian citizens access information about government schemes in their preferred language. This project was developed for a hackathon presentation on May 15, 2025, by Chari and Person A.
Project Overview
Suvrudhi provides an accessible, smartphone-friendly interface for users to:

Select a language (English, Hindi, Kannada, Telugu, Tamil).
Browse government schemes (e.g., PM-Kisan, Ayushman Bharat).
Listen to audio prompts with scheme details in their chosen language.

The app uses Flask for the backend, Jinja2 for templating, and integrates audio files generated via gTTS (Google Text-to-Speech). It features a visually engaging UI with animations, icons, and confetti effects to enhance user experience.
Features

Multilingual Support: Audio prompts and UI in 5 languages (English, Hindi, Kannada, Telugu, Tamil).
Audio Playback: Automatically plays welcome messages and scheme details using gTTS-generated .mp3 files.
Accessible UI: Numbered navigation (e.g., "1. Hindi") aligned with audio prompts ("Press 1 for Hindi").
Visual Enhancements:
Animated gradient background.
Interactive buttons with hover effects and Font Awesome icons.
Confetti animation on button clicks for a celebratory feel.


Responsive Design: Optimized for smartphones with a clean, user-friendly interface.
Easy Navigation: Back buttons to return to previous menus.

Prerequisites

Python 3.11: Ensure Python is installed on your system.
Git: For cloning and managing the repository.
Virtual Environment: Recommended for managing dependencies.
Cloud Storage: Audio files are hosted externally (e.g., Google Drive, AWS S3).

Installation

Clone the Repository:
git clone https://github.com/your-username/suvrudhi.git
cd suvrudhi


Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

Note: If requirements.txt is missing, install the required packages manually:
pip install flask


Host Audio Files:

The audio files are located in the audio/ directory.
Upload them to a cloud storage service (e.g., Google Drive, AWS S3).
Update the serve_audio route in flask_app/app.py with your cloud storage URL:cloud_base_url = "https://your-cloud-storage-url"




Run the App Locally:
cd flask_app
python app.py


The app will run at http://localhost:5000.



Usage

Access the App:

Open the app in a browser (e.g., http://localhost:5000 if running locally, or the deployed URL).
On a smartphone, access it via the local IP (e.g., http://192.168.1.100:5000) if testing on the same network.


Select a Language:

The welcome page plays a default English audio prompt.
Choose a language (e.g., "1. Hindi") to hear the welcome message in that language and proceed to the main menu.


Browse Schemes:

Select a scheme (e.g., "1. PM-Kisan") to hear its details in the chosen language.
Use the "Back" buttons to navigate to previous menus.



Deployment
The app is deployed on Render (or another hosting service) by Person A. To deploy:

Push Changes to GitHub:
git add .
git commit -m "Final updates for presentation"
git push origin main


Pull and Deploy on Render:

Person A should pull the changes:git pull origin main


If using Render with auto-deploy, the app will update automatically. Otherwise, manually redeploy via the Render dashboard.



Project Structure
suvrudhi/
│
├── flask_app/                 # Flask application directory
│   ├── app.py                 # Main Flask app
│   ├── static/                # Static assets (CSS, JS)
│   │   ├── css/styles.css     # Stylesheet with animations
│   │   └── js/script.js       # JavaScript for confetti and audio
│   └── templates/             # HTML templates
│       ├── index.html         # Language selection page
│       ├── main_menu.html     # Schemes menu page
│       └── scheme.html        # Scheme details page
│
├── audio/                     # Audio files for each language
│   ├── english/
│   ├── hindi/
│   ├── kannada/
│   ├── telugu/
│   └── tamil/
│
├── data/                      # JSON data for IVR script
│   └── ivr_script.json        # Scheme details and prompts
│
├── venv/                      # Virtual environment (not tracked)
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation

Credits

Charitha KR: Lead developer, responsible for app development, audio integration, and UI enhancements.
Soujanya V: Collaborator, responsible for deployment 
Tools Used:
Flask: Web framework.
gTTS: For generating audio prompts.
Font Awesome: For icons.
Canvas-Confetti: For celebratory animations.




https://github.com/user-attachments/assets/bc2ba45f-646e-4b30-b989-ebb2939481e1





License
This project is for a hackathon demo and is not licensed for public use. All rights reserved by Charitha and Soujanya, 2025.
