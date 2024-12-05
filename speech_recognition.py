import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog

# 初始化Tkinter
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 打开文件选择对话框
file_path = filedialog.askopenfilename(
    title='选择音频文件',
    filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")]
)

if file_path:
    recognizer = sr.Recognizer()

    # 从音频文件加载音频数据
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    # 使用Google的免费API进行语音识别，设置语言为俄语
    try:
        text = recognizer.recognize_google(audio_data, language='ru-RU')
        print("转录文本：", text)

        # 将转录的文本保存到文件
        with open("transcription_output.txt", "w", encoding='utf-8') as file:
            file.write(text)
        print("转录文本已保存到 'transcription_output.txt'。")

    except sr.UnknownValueError:
        print("Google Speech Recognition无法理解音频")
    except sr.RequestError as e:
        print("从Google Speech Recognition服务请求出错; {0}".format(e))
else:
    print("未选择文件")
