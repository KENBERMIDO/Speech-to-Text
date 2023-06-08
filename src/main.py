import speech_recognition as sr
import wave
import keyboard

r = sr.Recognizer() # Create a 'Recognizer' instance, to recognize speech
mic = sr.Microphone() # Create a mic source (set up your mic)
r.energy_threshold = 1500 # Define the

chat_log = "C:\conversation.txt"

while True:
    print("The program is now listening. Please speak.")
    with mic as source:
        audio = r.listen(source, timeout = None) # listen for the first phrase and extract it into audio data, no timeout
