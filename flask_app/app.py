from flask import Flask, render_template, request, send_from_directory
import json
import os

app = Flask(__name__)

# Load the IVR script JSON
with open('../data/ivr_script.json', 'r', encoding='utf-8') as file:
    ivr_script = json.load(file)

# Supported languages
LANGUAGES = ['english', 'hindi', 'kannada', 'telugu', 'tamil']

# Route for the homepage (language selection)
@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

# Route for the main menu (after language selection)
@app.route('/main_menu/<language>')
def main_menu(language):
    if language not in LANGUAGES:
        return "Invalid language", 400
    return render_template('main_menu.html', language=language, schemes=ivr_script['ivr_script']['schemes'])

# Route for scheme details
@app.route('/scheme/<language>/<scheme_name>')
def scheme_details(language, scheme_name):
    if language not in LANGUAGES:
        return "Invalid language", 400
    scheme = next((s for s in ivr_script['ivr_script']['schemes'] if s['name'].replace(" ", "_").lower() == scheme_name), None)
    if not scheme:
        return "Scheme not found", 404
    return render_template('scheme.html', language=language, scheme=scheme)

# Route to serve audio files
@app.route('/audio/<language>/<filename>')
def serve_audio(language, filename):
    return send_from_directory(f'../audio/{language}', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)