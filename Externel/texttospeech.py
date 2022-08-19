from gtts import gTTS
name = input("Enter the text")
name1 = gTTS(name,lang='en')
name1.save("texttospeech.mp3")