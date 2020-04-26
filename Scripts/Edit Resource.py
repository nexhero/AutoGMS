import time

timing = 0.2
# Edit resource in GameMaker Studio 2

#Input resource name
rcode,rinput = dialog.input_dialog("Edit Resource","Enter resource name")

engine.run_script("Activate GMS")
keyboard.send_keys("<ctrl>+t")
time.sleep(timing)

keyboard.send_keys(str(rinput))

time.sleep(timing)
system.exec_command('notify-send "GMS2 - Edit Resource"',False)

