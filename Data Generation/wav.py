# This file will Convert mp3 files to wav file
import os
import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt
from pydub import AudioSegment


import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt

import pylab

init_dir = "data/mp3/"
wav_dir = "data/wav/"
spec_dir = "data/spectrogram/"
m_spec_dir = "data/mel_spectrogram/"

folders = os.listdir(init_dir)

for i in folders:

    path = init_dir + i
    files = os.listdir(path)
    try:
        os.mkdir(wav_dir+i)
    except:
        pass
    for j in files:
        temp = path+'/'+j
        song = AudioSegment.from_mp3(temp)
        temp_name = wav_dir+i+'/'+j[:(len(j)-4)]+'.wav'
        song.export(temp_name,'wav')
    print(i)