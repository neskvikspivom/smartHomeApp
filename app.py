from classes import Hardware
import time
from guizero import App, PushButton, Text
tik = 0
k = 0
pin = 0

relay = Hardware.Relay(pin, False)




def water_on():
    if watering_text.value == 'hello':
        relay.on()
        watering_text.value = 'watering'
        time.sleep(5)
        watering_text.value = 'hello'







app = App(title="Hello world")

watering_text = Text(app, text='hello')

k = k + 1

watering_button = PushButton(app, text='start watering', command=water_on)

app.display()
