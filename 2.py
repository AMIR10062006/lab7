import pygame
import os
import keyboard


pygame.init()


def load_playlist_from_folder(folder_path):
    playlist = []
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):  
            playlist.append(os.path.join(folder_path, file))
    return playlist


def initialize_player(playlist):
    
    current_track_index = 0


    pygame.mixer.music.load(playlist[current_track_index])


    playing = False
    paused = False

    print("Controls: 'p' to play/pause, 's' to stop, 'n' for next track, 'q' to quit.")


    while True:
        if keyboard.is_pressed('p'):
            if not playing:
                pygame.mixer.music.play()
                playing = True
            else:
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False

        if keyboard.is_pressed('s'):
            if playing:
                pygame.mixer.music.stop()
                playing = False
                paused = False

        if keyboard.is_pressed('n'):
            current_track_index = (current_track_index + 1) % len(playlist)
            pygame.mixer.music.load(playlist[current_track_index])
            if playing:
                pygame.mixer.music.play()

        if keyboard.is_pressed('q'):
            pygame.quit()
            quit()


folder_path = input("Enter the path of the folder containing music files: ")

if os.path.exists(folder_path):
    
    playlist = load_playlist_from_folder(folder_path)

   
    initialize_player(playlist)
else:
    print("Folder not found.")
