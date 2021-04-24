#function for text to speech
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Isra.mp3')
    playsound('Isra.mp3')
