import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone(device_index=0)

print("Start Speaking")

with mic as source:
	audio = r.listen(source)


try:
	result = r.recognize_google(audio)
except sr.RequestError:
	exit("API is unreachable")

except sr.UnknownValueError:
	exit("Unable to recognize speech! ")


with open('my_speech.txt',mode='w') as file:
	file.write(result)

print("It has stored speech into text in my file")

