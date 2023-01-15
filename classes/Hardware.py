from gpiozero import OutputDevice, InputDevice

class Relay(OutputDevice):
    def __init__(self, pin, active_high):
        super(Relay, self).__init__(pin, active_high)

class waterLvl(InputDevice):
    def __init__(self, pin):
        super(waterLvl, self).__init__(pin)