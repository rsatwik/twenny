#!/usr/bin/env python
import os
import time
starttime = time.time()
def start():
    os.system("notify-send --hint int:transient:1 'Tweeny' \"It's time, look away for 20 seconds!\" && sleep 20 && notify-send --hint int:transient:1 'Tweeny' 'You can continue working now' > /dev/null")

while True:
    start()
    time.sleep(1200 - ((time.time() - starttime) % 1200.0))
