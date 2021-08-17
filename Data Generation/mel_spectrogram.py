# Code For Generating Mel Spectrogram

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


wav_folders = os.listdir(wav_dir)
for i in wav_folders:
    path = wav_dir + i
    wav_files = os.listdir(path)
    count = 1

    count1 = 1

    
    try:
        os.mkdir(m_spec_dir+i)
    except:
        pass
    print(i)
    for j in wav_files:
        temp = path+'/'+j
        rate, X = scipy.io.wavfile.read(temp)
        length = np.shape(X)[0]/float(rate)
        
        for k in range(1,6):
            try:
                temp_plot = m_spec_dir+i+'/'+str(count)+'.png'
                Y = X[rate*30*k:rate*60*k]       
                Y = np.mean(Y, axis=1)
                mel_spectrogram = librosa.feature.melspectrogram(Y, sr=rate, n_fft=2048, hop_length=512, n_mels=10)
                log_mel_spectrogram = librosa.power_to_db(mel_spectrogram)
        
                pylab.axis('off') 
                pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
                librosa.display.specshow(log_mel_spectrogram, sr=rate)
                pylab.savefig(temp_plot, bbox_inches=None, pad_inches=0)
                pylab.close()
                count+=1  

                
            except:
                break
        print(count1)
        count1+=1  
    print()