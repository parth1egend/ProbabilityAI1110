import os
from numpy import random
import pygame
from tkinter import Tk, Button, Label


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
    root.geometry('400x200')  # Set the size of the window (width x height)
    root.title('Music Player')
    
    text_label = Label(root, text='Hello World!')
    text_label.pack()
    text_label = Label(root, text='Randomized Music Player')
    text_label.pack()
    text_label = Label(root, text='The songs are in a random order.')
    text_label.pack()
    text_label = Label(root, text=' Use the buttons to navigate through them!')
    text_label.pack()
    next_button = Button(root, text='Next', command=next_song)
    # Position the button to the left with padding
    next_button.pack(side='left', padx=10, pady=10)

    previous_button = Button(root, text='Previous', command=previous_song)
    # Position the button to the right with padding
    previous_button.pack(side='right', padx=10, pady=10)

    root.mainloop()


# Replace with the path to your audio folder
folder_path = '/Users/parthajit/Desktop/projectfiles/audiofiles'
play_random_songs(folder_path)

