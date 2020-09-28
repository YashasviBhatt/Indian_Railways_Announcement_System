# Importing the libraries

import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
    '''function to convert text to speech and saving the audio inside a file'''
    txt = str(text)
    language = 'hi'                                                             # using google-hindi language
    audio = gTTS(text=txt, lang=language, slow=False)                           # using google text-to-speech
    audio.save(filename)

def mergeAudios(sounds):
    '''merge multiple audios'''
    combined_audio = AudioSegment.empty()                                       # creating an empty audio
    for sound in sounds:
        combined_audio += AudioSegment.from_mp3(f'.\\audios\{sound}')           # merging audio

    return combined_audio

def generateSkeleton():
    '''create fixed audio segments'''
    # importing audio
    audio = AudioSegment.from_mp3(r'.\audios\railway.mp3')                      # returns pydub.audio_segment.AudioSegment object

    # generating kripya dhyan deejiye audio
    start = 88000                                                               # in milliseconds
    end = 90200
    audioProcessed = audio[start:end]                                           # audio slicing
    audioProcessed.export(r'.\audios\01_kr_dh_de.mp3', format='mp3')            # saving sliced audio

    # generating se chal kar audio
    start = 91000                                                               # in milliseconds
    end = 92200
    audioProcessed = audio[start:end]                                           # audio slicing
    audioProcessed.export(r'.\audios\03_se_ch_ka.mp3', format='mp3')            # saving sliced audio

    # generating ke raste audio
    start = 94000                                                               # in milliseconds
    end = 95000
    audioProcessed = audio[start:end]                                           # audio slicing
    audioProcessed.export(r'.\audios\05_ke_ra.mp3', format='mp3')               # saving sliced audio

    # generating jaane wali gaadi sankhya audio
    start = 96200                                                               # in milliseconds
    end = 98900
    audioProcessed = audio[start:end]  # audio slicing
    audioProcessed.export(r'.\audios\07_ja_wa_ga_sa.mp3', format='mp3')         # saving sliced audio

    # generating kuchh hi samay me platform sankhya audio
    start = 105500                                                              # in milliseconds
    end = 108200
    audioProcessed = audio[start:end]                                           # audio slicing
    audioProcessed.export(r'.\audios\09_ku_hi_sa_me_pl_sa.mp3', format='mp3')   # saving sliced audio

    # generating par aa rhi hai audio
    start = 109000                                                              # in milliseconds
    end = 112150
    audioProcessed = audio[start:end]                                           # audio slicing
    audioProcessed.export(r'.\audios\11_pa_aa_rh_ha.mp3', format='mp3')         # saving sliced audio

def generateAnnouncement(filename):
    '''generate announcement sequence'''
    dF = pd.read_excel(filename)
    for index, item in dF.iterrows():
        # generating from city audio
        textToSpeech(item['from'], r'.\audios\02_fr_ci.mp3')
        # generating via city audio
        textToSpeech(item['via'], r'.\audios\04_vi_ci.mp3')
        # generating to city audio
        textToSpeech(item['to'], r'.\audios\06_to_ci.mp3')
        # generating train_number, train_name audio
        textToSpeech(f'{item["train_no"]}  {item["train_name"]}', r'.\audios\08_train.mp3')
        # generating platform audio
        textToSpeech(item['platform'], r'.\audios\10_platform.mp3')

        sounds = [file for file in os.listdir(r'.\audios')]                     # list evaluation to fetch all audios
        sounds.remove('railway.mp3')
        announcement = mergeAudios(sounds)
        announcement.export(f'.\\final_audios\\announcement[{item["train_no"]}{item["train_name"]}].mp3', format="mp3")    # exporting merged audio

    for file in sounds:
        os.remove(f'.\\audios\{file}')

if __name__ == '__main__':
    print('Please Wait Skeleton Audio is Processing...')
    generateSkeleton()
    print('Skeleton Audio Processed Successfully')
    print('Now Processing Other Audios')
    generateAnnouncement('announce_hindi.xlsx')
    print('Other Audios Processed Successfully')
    print('Audio Processing Complete')