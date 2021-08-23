import board
import digitalio
import storage
print('boot.py - start')
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
switch = digitalio.DigitalInOut(board.GP5)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP
if switch.value == False:
    print('Grounded, booting')
else:    
    print('Not grounded, disable usb')
    storage.disable_usb_drive()
    led.value = True
print('boot.py - done')
