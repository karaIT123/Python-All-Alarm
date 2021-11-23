from gpiozero import LEDCharDisplay, LED, Button
from time import sleep


class Alarm:
    char = LEDCharDisplay(19, 26, 20, 16, 12, 13, 6, dp=21, active_high=False)
    led = LED(18)
    button = Button(23)
    button1 = Button(25)
    button2 = Button(22)
    button3 = Button(27)
    button4 = Button(17)
    systemStatus = False
    alarmStatus = False
    sec = ""

    def __init__(self):
        self.Seg7 = Alarm.char
        self.Led = Alarm.led
        self.Button = Alarm.button
        self.Button1 = Alarm.button1
        self.Button2 = Alarm.button2
        self.Button3 = Alarm.button3
        self.Button4 = Alarm.button4
        self.AlarmStatus = Alarm.alarmStatus
        self.SystemStatus = Alarm.systemStatus
        self.Sec = Alarm.sec

        self.Seg7.value = '0'

    def initialize(self):
        if self.Button.is_pressed:
            if self.AlarmStatus:
                self.AlarmStatus = not self.AlarmStatus
                self.disarm()
            else:
                self.AlarmStatus = not self.AlarmStatus
                self.arm()

    def setPersmission(self):
        self.Button1.when_pressed = lambda: self.display("1")
        self.Button2.when_pressed = lambda: self.display("2")
        self.Button3.when_pressed = lambda: self.display("3")
        self.Button4.when_pressed = lambda: self.display("4")

    def unsetPermission(self):
        self.Button1.when_pressed = None
        self.Button2.when_pressed = None
        self.Button3.when_pressed = None
        self.Button4.when_pressed = None

    def arm(self):
        i = 0
        while i < 10:
            self.Seg7.value = f"{i}"
            sleep(1)
            i += 1
        self.AlarmStatus = True
        self.Seg7.value = 'A'
        self.setPersmission()

    def disarm(self):
        self.Led.off()
        i = 9
        while i > 0:
            self.Seg7.value = f"{i}"
            sleep(1)
            i -= 1
        self.AlarmStatus = False
        self.Seg7.value = '0'
        self.unsetPermission()

    def reset(self):
        self.Led.off()
        self.Seg7.value = "A"
        self.Sec = ""

    def display(self, val):
        if self.Sec != "":
            print('OK')
            self.reset()
        else:
            self.Seg7.value = val
            self.Sec = val

alarm = Alarm()
try:
    while True:
        alarm.initialize()
except KeyboardInterrupt:
    pass
