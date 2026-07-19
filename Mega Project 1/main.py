import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "fa199627df44470f9fa162902c6467d2"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def process_command(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif "open netflix" in c.lower():
      webbrowser.open("https://netflix.com")
   elif c.lower().startswith("play"):
      song= c.lower().split(" ")[1]
      link=music_library.music[song]
      webbrowser.open(link)
   

def fetch_news() -> None:
    """Fetch top 5 news headlines via NewsAPI and read them aloud."""
    url = (
        f"https://newsapi.org/v2/top-headlines"
        f"?language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    )
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        articles = data.get("articles", [])
        if not articles:
            speak("I could not find any news at the moment.")
            return
        speak("Here are the top headlines:")
        for i, article in enumerate(articles, 1):
            headline = article.get("title", "No title available")
            print(f"  {i}. {headline}")
            speak(headline)
    except Exception as e:
        print(f"News fetch error: {e}")
        speak("Sorry, I was unable to fetch the news right now.")
     
if __name__ == "__main__":
    speak("Initializing JARVIS, please wait...")
while True:  
    # listen for wake word "JARVIS"

    # obtain audio from the microphone
    r=sr.Recognizer()
    
    print("Processing ...")

# recognize speech using google speech recognition
    try:
        with sr.Microphone() as source:
          print("Listening ...")
          audio = r.listen(source,timeout=5,phrase_time_limit=4)
        word = r.recognize_google(audio)
        if  "jarvis" in word.lower():
          speak("Yah") 
     #   listen for user command
        with sr.Microphone() as source:
          print("Jarvis Activate and listening for your command ...")
          audio = r.listen(source)
          commmand = r.recognize_google(audio)
          process_command(commmand)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
