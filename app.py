from classes import Hardware
from datetime import datetime
from guizero import App, PushButton, Text

wlvl_pin = 0
relay_pin = 0

relay = Hardware.Relay(relay_pin, False)
wlvl = Hardware.waterLvl(wlvl_pin)



def water_on():
    while wlvl.value == 0:
        relay.on()
    else:
        relay.off()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        last_watering_time.value == current_time






app = App(title="Hello world")

watering_text = Text(app, text='hello')

last_watering_time = Text(app)
last_watering_time.repeat(86400000, water_on)

watering_button = PushButton(app, text='start watering', command=water_on)


app.display()
