import pygame
from pygame import mixer
import keyboard

fileName = "Owl City  Carly Rae Jepsen  Good Time Lyrics"
fileNameExtension = f"{fileName}.mp3"
path = f"D:\\CC\\Tom\\music\\{fileNameExtension}"

# Initialize the mixer module
mixer.init()

# Load the audio file
mixer.music.load(path)

# Play the audio file
mixer.music.play()

# Variable to keep track of the music state
paused = False

# Loop until "q" key is pressed
while True:
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('\nQuit')
        break  # finish the loop
    if keyboard.is_pressed('p'):  # if key 'p' is pressed
        if paused:
            mixer.music.unpause()
            paused = False
        else:
            mixer.music.pause()
            paused = True
    if not mixer.music.get_busy() and not paused:
        # Play the audio file again
        mixer.music.play()
