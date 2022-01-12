from pynput import keyboard
import winsound

winsound.PlaySound(r'C:\sound.wav', winsound.SND_ASYNC)

winsound.PlaySound(None, winsound.SND_PURGE)
