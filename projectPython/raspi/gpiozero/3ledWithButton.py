from gpiozero import LED, Button

led = LED(19)
button = Button(26)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
