import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#engine the speed
engine.setProperty('rate', 100)
engine.setProperty('volume', 1)
engine.say("hello everyone welcome to AIML course")
engine.runAndWait()
