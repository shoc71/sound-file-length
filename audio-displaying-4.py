import os
from mutagen.mp3 import MP3# - fuk dis shit, only accept strings with .mp3 at the endS
from mutagen.wave import WAVE#Ogg doesnt exist on mutagen library

def audio_start():
    print("this is a program that will display all the music lengths that you want")
    print("Example - C:\\Users\\Sonu.Singh\\Downloads")
    print("complete the following downloads on your computer on cmd")
    print("pip install os")
    print("pip install mutagen")
    print("created by mystery_orbs")

    user_input = r"C:\users\sonu.singh\music"

    filepath = user_input #this can be removed
    for sound_file in os.listdir(filepath):# - mutagen can't accept lists
        filenames = os.path.join(filepath, sound_file) #the most important step / slapping the path and file together
        if sound_file.endswith(".mp3"):
            audio = MP3(filenames)
            print(give_song(audio, sound_file))
        elif sound_file.endswith(".wav"):
            audio = WAVE(filenames)
            print(give_song(audio, sound_file))
        else:
            print("not a sound file")

    return "finished"
    
def give_song(audio_in, sound_file):
    song_length = audio_in.info.length
    song_length = str(audio_in.info.length)
    song = sound_file + " - "+ song_length
    return song

if __name__ == "__main__":#when you start the program, do the following
    print(audio_start()) 