import keyboard
import pyautogui

print("Bu yazılım Taha Sengul adına özel olarak uretilmistir.")

while True:
    try:
        if keyboard.is_pressed('insert'):
            print("Başladı")
            while True:
                pyautogui.write("z3")
                if keyboard.is_pressed('home'):
                    print("Duraklatıldı")
                    break
        else:
            pass
    except:
        break