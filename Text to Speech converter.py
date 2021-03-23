#import the pyttsx library
import pyttsx3

#initialization
engine = pyttsx3.init()

#testing
engine.say('Hey Rhee')
engine.say('How is your day going?')
engine.say('Have you had anything to eat yet?')
engine.say('Did you resolve the OpenGL issue?')
engine.say('What are you up to now?')
engine.runAndWait()
engine.stop()

