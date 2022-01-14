
from playsound import playsound
import threading
from pynput import keyboard
import winsound


path = "key_press_sound2.wav"
path2 = "key_press_sound.wav"


def play_sound():
    winsound.PlaySound(path2, winsound.SND_ASYNC)

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


def start():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        thread1 = threading.Thread(target=listener.join)
        thread1.start()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    thread2 = threading.Thread(target=listener.start)
    thread2.start()
    input()


