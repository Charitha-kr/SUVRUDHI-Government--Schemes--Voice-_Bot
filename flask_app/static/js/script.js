// Function to play welcome audio in selected language
function playWelcomeAudio(language) {
    const audio = document.getElementById('welcome-audio');
    const source = document.getElementById('welcome-source');

    if (!audio || !source) return;

    source.src = `/audio/${language}/welcome_message_${language}.mp3`;
    audio.load();
    audio.play().catch(error => {
        console.error("Audio playback failed:", error);
    });
}

// Multilingual rotating description
document.addEventListener("DOMContentLoaded", () => {
    const descriptions = [
        "This website helps you understand Indian government schemes.",          // English
        "यह वेबसाइट आपको भारतीय सरकारी योजनाओं को समझने में मदद करती है।",      // Hindi
        "ಈ ವೆಬ್‌ಸೈಟ್ ನಿಮಗೆ ಭಾರತೀಯ ಸರ್ಕಾರದ ಯೋಜನೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.", // Kannada
        "ఈ వెబ్‌సైట్ భారత ప్రభుత్వ పథకాల గురించి మీకు అర్థం చేసుకోవడంలో సహాయపడుతుంది.", // Telugu
        "இந்த இணையதளம் இந்திய அரசுத் திட்டங்களைப் புரிந்து கொள்ள உதவுகிறது."       // Tamil
    ];

    let currentIndex = 0;
    const rotator = document.getElementById("description-rotator");

    if (!rotator) return;

    // Initialize with first description
    rotator.textContent = descriptions[currentIndex];
    rotator.style.opacity = 1;

    // Function to rotate text with fade effect
    function rotateText() {
        // Fade out
        rotator.style.opacity = 0;

        setTimeout(() => {
            // Update text after fade-out
            currentIndex = (currentIndex + 1) % descriptions.length;
            rotator.textContent = descriptions[currentIndex];

            // Fade in
            rotator.style.opacity = 1;
        }, 500); // Time matches the fade transition
    }

    // Rotate every 4 seconds
    setInterval(rotateText, 4000);
});
