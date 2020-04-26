# Create Objects, Sprites, Scripts, etcs on GMS2 from emacs
import time
window_title = "Create Resources - GMS2"

resources_list = ["Sprite","Tile Sets","Sound","Path","Script","Shaders","Font","Timeline","Object","Room"]

retCode, choice = dialog.list_menu(resources_list,window_title)
window.wait_for_focus(window_title)
window.resize_move(window_title, xOrigin=-1, yOrigin=-1, width=-1, height=450, matchClass=False)


if(len(str(choice))>0):
    #Set GameMakerStudio 2 Focus
    engine.run_script("Activate GMS")
    if(choice == "Sprite"):
        keyboard.send_keys("<alt>+s")
    elif(choice == "Tile Set"):
        keyboard.send_keys("<alt>+b")
    elif(choice == "Sound"):
        keyboard.send_keys("<alt>+u")
    elif(choice == "Path"):
        keyboard.send_keys("<alt>+p")
    elif(choice == "Script"):
        keyboard.send_keys("<alt>+c")
    elif(choice == "Shaders"):
        keyboard.send_keys("<alt>+a")
    elif(choice == "Font"):
        keyboard.send_keys("<alt>+f")
    elif(choice == "Timeline"):
        keyboard.send_keys("<alt>+t")
    elif(choice == "Object"):
        keyboard.send_keys("<alt>+o")
    elif(choice == "Room"):
        keyboard.send_keys("<alt>+r")
    
    system.exec_command('notify-send "GMS2 - Resource has been created"',False)