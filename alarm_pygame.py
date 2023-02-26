#!/usr/bin/env python3

# The sound player script.

from gpiozero import Button
import pygame
import datetime
import time

button = Button(21)

def play_the_sound(sound_file='/home/kudep/Documents/watch_home_dog/alarm.wav'):
    # Play the sound.
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    playing = sound.play()
    while playing.get_busy():
        pygame.time.delay(100)

def wait_button(gpio_id=21):
    print("run wait_button")
    button.wait_for_press()
    # button.wait_for_release()

def setup_alarm(action, repeat_n=10):
    print("run setup_alarm")
    for i in range(repeat_n):
        wait_button()
        action()
        time.sleep(1)

def daily_cock_alarm(cock_datetime="01:00", action=play_the_sound):
    print("run daily_cock_alarm")
    while True:
        setup_alarm(action)
        while datetime.datetime.now().strftime("%H:%M") != cock_datetime:
            time.sleep(1)

if __name__ == '__main__':
    # This script is being executed directly. Play the sound right away!
    daily_cock_alarm("01:00", play_the_sound)


