import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as source:
    print('Listening....')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    if 'jarvis' in command:
        print(command)