""" This module uses pyttsx3 to speak as the first step in every pyttsx3 script is this so I am making a module for it."""

Class Speak:
    """ I am bad in classes but since pypi requries one I'll give it a go """
    import pyttsx3

    self.engine = pyttsx3.init() # This will initialize pyttsx3

    def speak(self,audio):
        """ The main Function"""
        self.engine.say(audio)
        self.engine.runAndWait()


# Hopefully this will run
speak("Hello user thanks for downloading this module")
