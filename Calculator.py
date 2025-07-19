from matplotlib.pylab import f
import wolframalpha
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)

# Speak Function
def speak(audio):
    """Function to convert text to speech."""
    engine.say(audio)
    engine.runAndWait()   


def WolfRamALpha(query):
    apikey = "5X6URG-723QVP3HTJ"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer 
    except:
        speak("Your Value is not answerable")
        
def Calc(query):
    
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("multiply","*")
    Term = Term.replace("divide","/")
    Term = Term.replace("subtract","-")
    
    Final = str(Term)
    
    try:
        
        result = WolfRamALpha(Final)
        print(f"{result}")
        speak(result)
    except:
        speak("The value is not answerable")