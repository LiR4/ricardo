# Our main file

import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

# Abri o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        
        print(r.recognize_google(audio))
