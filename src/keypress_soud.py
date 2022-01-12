
from playsound import playsound
import threading
from pynput import keyboard
import winsound

path = r"C:\Users\Iiryu\Documents\GitHub\notepad\src\key_press_sound.wav"


def play_sound():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound(path, winsound.SND_ASYNC)


def on_press(key):
    try:
        play_sound()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
