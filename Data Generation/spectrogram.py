#Code to generate Spectrogram
import os
import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt
from pydub import AudioSegment

init_dir = "data/mp3/"
wav_dir = "data/wav/"
spec_dir = "data/spectrogram/"

wav_folders = os.listdir(wav_dir)
for i in wav_folders:
    path = wav_dir + i
    wav_files = os.listdir(path)
    count = 1
    
    try:
        os.mkdir(spec_dir+i)
    except:
        pass
    print(i)
    count1 = 1
    
    for j in wav_files:
        print(count1)
        count1 +=1
        temp = path+'/'+ j
        rate, X = scipy.io.wavfile.read(temp)
        length = np.shape(X)[0]/float(rate)
        
        for k in range(1,6):
            try:
                temp_plot = spec_dir+i+'/'+str(count)+'.png'
                Y = X[rate*30*k:rate*60*k]       
                Y = scipy.mean(Y, axis=1)
                plt.specgram(Y, Fs=rate)
                plt.axis('off')
                plt.savefig(temp_plot,bbox_inches='tight')
                plt.close()
                count+=1  
            except:
                break