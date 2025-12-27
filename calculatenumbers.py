import wolframalpha
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Query WolframAlpha
def WolfRamAlpha(query):
    apikey = "E2HK4P-9WJG6JLJ3G"  # Replace with your actual key
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except StopIteration:
        # If there's no result in the query
        raise ValueError("No answer returned from WolframAlpha")


# Calculator handler
def Calc(query):
    Term = str(query)
    Term = Term.lower().replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term.strip())

    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)
    except Exception as e:
        print(f"Error: {e}")
        speak("The value is not answerable")
