"""
This module uses pyttsx3 to speak as the first step in every pyttsx3 app is this so I am making a module for it.
"""

import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  
  
 # Hopefully this will run
speak("Hello user thanks for downloading this module")
