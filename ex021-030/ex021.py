import pygame
pygame.init()
pygame.mixer.music.load('ex021-030/ex021.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()

input()
pygame.event.wait()
