import speech_recognition as sr

import os
import warnings


from pydub import AudioSegment
from pydub.silence import split_on_silence
from tkinter import *
from tkinter import filedialog
from pydub.utils import which
AudioSegment.converter = which("ffmpeg")

root = Tk()
r = sr.Recognizer()


def silence_based_conversion(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "

                whole_text += text
    # return the text for all chunks detected
    return whole_text


def text():
    """get the path of the audio file and recognizes the audio and convert it to text and return in a .txt file"""

    global name

    AUD = filedialog.askopenfilename()
    print(silence_based_conversion(AUD))


root.configure(bg='light blue')

global label_aud_txt
global aud_txt_covbutton
global aud_txt_back
global aud_tex1
global aud_tex2
global name
global Lable_name

# entry section


# label section

aud_tex1 = Label(root, text='AUDIO TO TEXT', font=("Phosphate", 30), bg='light blue')
aud_tex2 = Label(text='AUDIO RECORDING TECHNOLOGY WAS HIDDEN FROM REST OF THE WORLD FOR\n 15 YEARS BY NAZI REGIME',
                 font=('normal', 12), bg='light blue')
label_aud_txt = Label(text="click the button below to convert", font=('normal', 26), bg='light blue')

# button section

aud_txt_covbutton = Button(text="browse...", font=("Herculanum",), activebackground='cornsilk2', command=text)
aud_txt_back = Button(root, text=">>")

# The Grid geometry manager puts the widgets in a 2-dimensional table

label_aud_txt.grid(row=3, column=0, padx=5)
aud_txt_covbutton.grid(row=4, column=0, pady=20)
aud_tex1.grid(row=0, column=0, padx=168, pady=25)
aud_tex2.grid(row=5, column=0)
aud_txt_back.grid(row=6, column=1)

root.mainloop()