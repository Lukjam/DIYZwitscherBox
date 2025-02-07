# Bibliotheken laden
import time
from picozero import Button
from picodfplayer import DFPlayer
from machine import Pin

# Initialisierung DFPlayer (UART, TX-Pin, RX-Pin, Busy-Pin)
player = DFPlayer(0, 16, 17, 18)
time.sleep(1)
player.setVolume(20) # Lautstärke einstellen: 0 bis 30
ldr = machine.ADC(27)
last = ldr.read_u16()
while True:
    current = ldr.read_u16()
    if (last < current):
        if ((last+200) < current):
            if player.queryBusy() == False:                                                                                        
                player.playTrack(1,1)
    elif (last > current):
        if ((last-200) > current):
            if player.queryBusy() == False:
                player.playTrack(1,1)
    last = current
    time.sleep(10)