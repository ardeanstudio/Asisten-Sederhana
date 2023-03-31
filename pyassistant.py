import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# inisialisasi pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 untuk perempuan dan 0 untuk laki-laki


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Mengenali...")
        query = r.recognize_google(audio, language='en-in')
        print("User Mengatakan:" + query + "\n")
    except Exception as e:
        print(e)
        speak("Saya tidak mengerti")
        return "Tidak Ada"
    return query


if __name__ == '__main__':

    speak("Asisten Ardean Aktiv")
    speak("Ada yang bisa saya bantu?")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("Menurut wikipedia")
            speak(results)
        elif 'Apakah anda' in query:
            speak("Saya Ardean Asisten dikembangkan oleh Ardean Studio")
        elif 'buka youtube' in query:
            speak("Membuka youtube")
            webbrowser.open("youtube.com")
        elif 'buka google' in query:
            speak("membuka google")
            webbrowser.open("google.com")
        elif 'buka github' in query:
            speak("membuka github")
            webbrowser.open("github.com")
        elif 'buka stackoverflow' in query:
            speak("membuka stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'buka spotify' in query:
            speak("membuka spotify")
            webbrowser.open("spotify.com")
        elif 'buka whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\ardean\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'mainkan musik' in query:
            speak("membuka musik")
            webbrowser.open("spotify.com")
        elif 'mainkan musik' in query:
            speak("membuka musik")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("membuka local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("membuka local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("membuka local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            exit(0)
