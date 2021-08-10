
from speak import Speak

client = Speak()
client.speak("Hello") # Remove the Hello string with any other string ##

#eg:
def input_speak(name):
  client.speak(f"Hi {name}")
 
#use the function like:
name1 = input("What's your name?: ")
input_speak(name1)
