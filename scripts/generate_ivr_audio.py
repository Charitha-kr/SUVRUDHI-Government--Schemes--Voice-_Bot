from gtts import gTTS
import json
import os

# Load the IVR script JSON with UTF-8 encoding
with open('../data/ivr_script.json', 'r', encoding='utf-8') as file:
    ivr_script = json.load(file)

# Language codes for gTTS
lang_codes = {
    "english": "en",
    "hindi": "hi",
    "kannada": "kn",
    "telugu": "te",
    "tamil": "ta"
}

# Base directory for audio files
audio_base_dir = "../audio"

# Generate audio for welcome message
for lang, text in ivr_script["ivr_script"]["welcome_message"].items():
    audio_dir = os.path.join(audio_base_dir, lang)
    os.makedirs(audio_dir, exist_ok=True)  # Create language directory if it doesn't exist
    tts = gTTS(text, lang=lang_codes[lang])
    audio_path = os.path.join(audio_dir, f"welcome_message_{lang}.mp3")
    tts.save(audio_path)
    print(f"Generated: {audio_path}")

# Generate audio for main menu
for lang, text in ivr_script["ivr_script"]["main_menu"].items():
    audio_dir = os.path.join(audio_base_dir, lang)
    tts = gTTS(text, lang=lang_codes[lang])
    audio_path = os.path.join(audio_dir, f"main_menu_{lang}.mp3")
    tts.save(audio_path)
    print(f"Generated: {audio_path}")

# Generate audio for each scheme prompt
for scheme in ivr_script["ivr_script"]["schemes"]:
    scheme_name = scheme["name"].replace(" ", "_").lower()  # e.g., "PM-Kisan" -> "pm_kisan"
    for lang, text in scheme["prompt"].items():
        audio_dir = os.path.join(audio_base_dir, lang)
        tts = gTTS(text, lang=lang_codes[lang])
        audio_path = os.path.join(audio_dir, f"{scheme_name}_{lang}.mp3")
        tts.save(audio_path)
        print(f"Generated: {audio_path}")