from gtts import gTTS
import os
from playsound import playsound


voice=input("Enter text to speak:\n")
gTTS(text=voice).save('speak.mp3')
playsound('speak.mp3')
if os.path('speak.mp3'):
    os.remove('speak.mp3')
else:
    print('File Does Not Exist')
