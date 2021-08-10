""" This module uses pyttsx3 to speak as the first step in every pyttsx3 script is this so I am making a module for it."""
import pyttsx3

class Speak:

  def __init__(self):
    self.engine = pyttsx3.init()

  def speak(self,audio):

    self.engine.say(audio)
    self.engine.runAndWait()

client = Speak()
client.speak("Hello")
