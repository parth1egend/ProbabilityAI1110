import os
import random
import pygame
from tkinter import Tk, Button

def play_random_songs(folder_path):
    audio_files = os.listdir(folder_path)
    random.shuffle(audio_files)
    current_index = 0

    def startsong():
        nonlocal current_index

        audio_file = audio_files[current_index]
        if audio_file.endswith('.mp3') or audio_file.endswith('.wav'):
            audio_path = os.path.join(folder_path, audio_file)
            print(f'Playing: {audio_path}')
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

    def next_song():
        nonlocal current_index
        pygame.mixer.music.stop()
        current_index = (current_index + 1) % len(audio_files)
        startsong()

    def previous_song():
        nonlocal current_index
        pygame.mixer.music.stop()
        current_index = (current_index - 1) % len(audio_files)
        startsong()

    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.75)  # Adjust the volume as desired

    startsong()

    root = Tk()
    next_button = Button(root, text='Next', command=next_song)
    next_button.pack()
    previous_button = Button(root, text='Previous', command=previous_song)
    previous_button.pack()
    root.mainloop()

folder_path = '/Users/parthajit/Desktop/projectfiles/audiofiles'  # Replace with the path to your audio folder
play_random_songs(folder_path)


