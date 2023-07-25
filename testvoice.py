import speech_recognition as sr
r = sr.Recognizer()
# 使用麦克风录音
with sr.Microphone() as source:
    print("请说话：")
    audio = r.listen(source)

# 将语音转换为文本
try:
    text = r.recognize_google(audio, language='zh-CN')
    print("你说的是：" + text)
except sr.UnknownValueError:
    print("无法识别你的语音")
except sr.RequestError as e:
    print("无法连接到Google API，错误原因：" + str(e))