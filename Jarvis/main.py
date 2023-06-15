import os
import random
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
def run():
    try:
        while True:
            r = sr.Recognizer()
            voice = pyttsx3.init()
            with sr.Microphone(device_index=2) as source:
                print('Скажите что-нибудь. . .')
                audio = r.listen(source)

            speech = r.recognize_google(audio, language="ru_RU").lower()
            print("Вы сказали :" + speech)
            hello = [
                "Приветcтвую , сэр",
                "Здравствуйте сэр",
                "Доброго дня вам сэр"
            ]
            if speech.find("пока") >= 0 or speech.find("прощай") >= 0:
                voice.say("Досвидания , сэр")
                voice.runAndWait()
                break
            elif speech.find('спасибо') >= 0:
                voice.say('Всегда пожалуйста')
                voice.runAndWait()
            elif speech.find("привет") >= 0:
                voice.say(random.choice(hello))
                voice.runAndWait()
            elif speech.find("музыка") >= 0 or speech.find("музыку") >= 0:
                webbrowser.open_new("https://www.youtube.com/watch?v=iubSQbAeb9c&t=1s")
                voice.say("Выполняю")
                voice.runAndWait()
            elif speech.find("ошибка в коде") >= 0:
                webbrowser.open_new("https://ru.stackoverflow.com/")
                voice.say("Сейчас исправим кэп")
                voice.runAndWait()
            elif speech.find("ютуб") >= 0 or speech.find("youtube") >= 0:
                webbrowser.open_new("https://www.youtube.com/")
                voice.say("есть сэр")
                voice.runAndWait()
            elif speech.find("как дела") >= 0:
                voice.say("отлично , сэр")
                voice.runAndWait()
            elif speech.find("телеграм") >= 0 or speech.find("telegram") >= 0:
                webbrowser.open_new('https://web.telegram.org/k/')
                voice.say("Выполняю кэп")
                voice.runAndWait()
            elif speech.find("открой google") >= 0:
                voice.say("Выполняю сэр")
                voice.runAndWait()
                subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            elif speech.find("Дискорд") >= 0 or speech.find("discord") >= 0:
                voice.say("есть сэр")
                voice.runAndWait()
                webbrowser.open_new('https://discord.com/channels/@me')
            elif speech.find('диагностика системы') >= 0:
                voice.say('готово')
                voice.runAndWait()
                os.system('taskmgr')
            elif speech.find('steam') >= 0:
                webbrowser.open_new('https://store.steampowered.com/?l=russian')
                voice.say('Сделано , сэр')
                voice.runAndWait()
            elif speech.find('джарвис') >= 0:
                webbrowser.open_new("http://www.google.com/search?q=" + speech[7::])
                voice.say('Выполняю')
                voice.runAndWait()
            else:
                pass
    except:
        run()
run()