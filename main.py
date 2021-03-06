import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
import os
import random
from gtts import gTTS
from playsound import playsound


r = sr.Recognizer() # ses algılayıcı tanımlandı 

def record_audio(ask = False):
    with sr.Microphone() as source: # mikrofon dinleme
        if ask:
            speaking(ask)
        audio = r.listen(source) # dinlendi
        voice_data = ""
        try: # ses düzgün algılanırsa
            voice_data = r.recognize_google(audio, language = "tr-TR")  # kullanıcının söylediği kelime/cümle = voice_data oldu

        except sr.UnknownValueError: # anlaşılmazsa
            speaking("Ne Dediğini Anlayamadım!")

        except sr.RequestError: # serviste hata çıkarsa
            speaking("Özür Dilerim, Şu Anda Çalışamıyorum!")
        return voice_data


def respond(voice_data): # kullanıcıya yanıt
    if "nasılsın" in voice_data:
        speaking("İyiyim, Sen Nasılsın?")
    if "nasıl gidiyor" in voice_data:
        speaking("İyi gidiyor")
    if "saat kaç" in voice_data:
        speaking(datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice_data:
        search = record_audio("Ne Aramak İstiyorsun?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speaking(f"{search} Araması Sonucunda Bunları Buldum")
    if "görüşürüz" in voice_data:
        speaking("Görüşürüz")
        exit()

def speaking(audio_string):
    tts = gTTS(audio_string, lang="tr") # text to speech 
    rand = random.randint(1,10000) # ses dosyasının ismi için
    file = "audio-"+str(rand)+".mp3" # ses dosyasının ismi için
    tts.save(file)
    playsound(file)
    os.remove(file) # ses dosyasını daha sonra karışmasın diye siliyor



speaking("sana nasıl yardımcı olabilirim")
time.sleep(1)
while 1:  
    voice_data = record_audio() 
    print(voice_data)
    respond(voice_data)


