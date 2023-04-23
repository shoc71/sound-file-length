import os
from mutagen.mp3 import MP3# - fuk dis shit, only accept strings with .mp3 at the endS
from mutagen.wave import WAVE#Ogg doesnt exist on mutagen library

print("this is a program that will display all the music lengths that you want")
print("Example - C:\\Users\\Sonu.Singh\\Downloads")
print("complete the following downloads on your computer on cmd")
print("pip install os")
print("pip install mutagen")
print("\ncreated by Mystorbius \n")
user_input1 = input("have you done these install? (Y/N): ")

def audio_duration_mp3(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length # calculate in seconds
    length %= 60
    millisec = length * 1000
    round(millisec,2)
    return hours, mins, seconds, millisec  # returns the duration

def audio_duration_wav(length):
    hours = length // 3600  # calculate in hours
    #length %= 3600
    mins = length // 60  # calculate in minutes
    #length %= 60
    seconds = length # calculate in seconds
    #length %= 60
    millisec = length * 900
    round(millisec,2)
    return hours, mins, seconds, millisec  # returns the duration

while user_input1 != "quit":
    if user_input1 in ["no","nah","na","n"]:
        print("download theses first on cmd and type them out")
        break
    user_input = input("enter filepath here : ")
    print("\nyou entered - " + user_input)
    if user_input in ["no","nah","na","n"]:
        print("invalid filepath")
        break

    filepath = user_input #this can be removed
    filepath = r"C:\Users\Sonu.Singh\Desktop\mystorbius\test"
    for sound_file in os.listdir(filepath):# - mutagen can't accept lists
        filenames = os.path.join(filepath, sound_file) #the most important step / slapping the path and file together
        if sound_file.endswith(".mp3"):
            audio = MP3(filenames)
            length = int(audio.info.length)
            hours, mins, seconds, millisec  = audio_duration_mp3(length)
            print('{} - Total Duration: {}:{}:{}:{}'.format(sound_file,hours, mins, seconds, millisec))
        elif sound_file.endswith(".wav"):
            audio = WAVE(filenames)
            length = int(audio.info.length)
            hours, mins, seconds, millisec  = audio_duration_wav(length)
            print('{} - Total Duration: {}:{}:{}:{}'.format(sound_file,hours, mins, seconds, millisec))
        else:
            print("no sound files found")
    user_input1 = input("have you done these install? (Y/N): ")