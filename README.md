# JARVIS AI Assistant

A powerful voice-controlled AI assistant built with Python, featuring a wide range of functionalities from basic voice commands to advanced tasks like scheduling, calculations, news reading, and more.

## Features

### Core Functionality
- **Voice Recognition**: Uses Google Speech Recognition for voice commands
- **Text-to-Speech**: Powered by pyttsx3 for natural voice responses
- **Wake Word Detection**: Responds to "wake up" command to activate

### Available Commands
- **Greeting & Basic Interaction**:
  - Wake up JARVIS
  - Basic conversations (hi, how are you, thank you)

- **System Control**:
  - Change password
  - Shutdown system
  - Volume control (up/down)
  - Take screenshots
  - Open/close applications

- **Productivity**:
  - Schedule daily tasks
  - Set alarms
  - Focus mode (blocks distractions)
  - Remember notes/messages

- **Information & Search**:
  - Google search
  - YouTube search
  - Wikipedia search
  - Latest news reading
  - Weather information
  - Temperature updates

- **Entertainment**:
  - Play games
  - Open camera for photos
  - Music control (play/pause/mute)

- **Communication**:
  - WhatsApp messaging
  - Translation services

- **Utilities**:
  - Calculator with WolframAlpha integration
  - Internet speed testing
  - IPL cricket scores
  - Dictionary/app opening

## Installation

### Prerequisites
- Python 3.7+
- Windows OS (currently optimized for Windows)
- Microphone for voice input
- Speakers/headphones for audio output

### Required Libraries
Install the following Python packages:
```
pip install speechrecognition
pip install pyttsx3
pip install pyautogui
pip install requests
pip install beautifulsoup4
pip install wolframalpha
pip install pygame
pip install plyer
pip install speedtest-cli
```

### Setup
1. Clone or download the project files
2. Install all required dependencies
3. Set up your WolframAlpha API key in `config.py`
4. Run the main script: `python jarvis_main.py`
5. Enter the password when prompted
6. Say "wake up" to activate JARVIS

## Usage

### Starting JARVIS
1. Run `jarvis_main.py`
2. Enter the correct password
3. Say "wake up" to activate the assistant

### Voice Commands
- Speak clearly and naturally
- Start commands with "JARVIS" or just speak normally after wake up
- Examples:
  - "JARVIS, what time is it?"
  - "Check internet speed"
  - "Set an alarm"
  - "Play a game"

### Password Protection
- Default password stored in `Password.txt`
- Change password using voice command: "change password"

## File Structure

```
├── jarvis_main.py          # Main JARVIS application
├── JARVIS.py              # Basic voice recognition demo
├── GreetME.py             # Greeting functionality
├── calculatenumbers.py    # Calculator with WolframAlpha
├── config.py              # WolframAlpha API configuration
├── alarm.py               # Alarm functionality
├── Dictapp.py             # Dictionary and app management
├── FocusGraph.py          # Focus tracking visualization
├── FocusMode.py           # Focus mode implementation
├── game.py                # Game functionality
├── installer.py           # Installation utilities
├── internet_speed.py      # Internet speed testing
├── INTRO.py               # Introduction script
├── keyboard.py            # Keyboard control functions
├── NewsRead.py            # News reading functionality
├── SearchNow.py           # Search utilities (Google, YouTube, Wikipedia)
├── Translator.py           # Translation services
├── Whatsapp.py            # WhatsApp messaging
├── Alarmtext.txt          # Alarm data storage
├── focus.txt              # Focus mode data
├── Remember.txt           # Notes/reminders storage
├── tasks.txt              # Daily tasks storage
├── Password.txt           # Password storage
├── PyWhatKit_DB.txt       # WhatsApp database
├── notification.mp3       # Notification sound
├── jarvis.mp3             # JARVIS activation sound
├── ss.jpg                 # Screenshot storage
├── JARVIS GUI.gif         # GUI demonstration
├── jarvis.gif.gif         # Animation files
├── .gitignore             # Git ignore rules
├── qodana.yaml            # Code quality configuration
└── README.md              # This file
```

## Configuration

### WolframAlpha API
- Get your API key from [WolframAlpha Developer Portal](https://developer.wolframalpha.com/)
- Replace the API key in `config.py` and `calculatenumbers.py`

### Customization
- Modify voice settings in `GreetME.py` and `jarvis_main.py`
- Adjust recognition sensitivity in the main script
- Add new commands by extending the command handling logic

## Troubleshooting

### Common Issues
1. **Microphone not detected**: Ensure microphone is properly connected and permissions granted
2. **Speech not recognized**: Speak clearly, check internet connection for Google API
3. **WolframAlpha errors**: Verify API key is correct and has sufficient queries remaining
4. **Module import errors**: Ensure all required packages are installed

### Voice Recognition Tips
- Use a good quality microphone
- Speak in a quiet environment
- Speak clearly and at normal pace
- Ensure stable internet connection

## Contributing

Feel free to contribute to the project by:
- Adding new features
- Improving voice recognition
- Fixing bugs
- Optimizing performance
- Adding support for other platforms

## License

This project is open-source. Please check individual file headers for specific licensing information.

## Disclaimer

This AI assistant is for educational and personal use. Ensure compliance with local laws and regulations when using automation features. The developers are not responsible for any misuse or damage caused by the software.

---

**Developed with ❤️ using Python**
