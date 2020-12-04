"""
This module uses pyttsx3 to speak as the first step in every pyttsx3 script is this so I am making a module for it.
"""
Class Speak:
    import pyttsx3

    self.engine = pyttsx3.init()

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()


# Hopefully this will run
speak("Hello user thanks for downloading this module")
