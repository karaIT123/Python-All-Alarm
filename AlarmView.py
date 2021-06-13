import tkinter as tk
import gpiozero as gp
from time import sleep


class tkForm:
    char = gp.LEDCharDisplay(19, 26, 20, 16, 12, 13, 6, dp=21, active_high=False)
    led = gp.LED(18)
    button = gp.Button(23)
    buttonSec = gp.Button(25)
    systemStatus = False
    alarmStatus = False

    def __init__(self, root):
        self.Seg7 = tkForm.char
        self.Led = tkForm.led
        self.Button = tkForm.button
        self.ButtonSec = tkForm.buttonSec
        self.AlarmStatus = tkForm.alarmStatus
        self.SystemStatus = tkForm.systemStatus

        self.root = root
        self.labelTitre = tk.Label(root, text="Alarm")
        self.labelTitre.grid(row=0, column=0, columnspan=5)
        self.labelTitre.grid(padx=5, pady=5)

        self.Z1 = tk.Button(root, text="Zone 1", width=10, height=5, bg='orange', fg="white",
                            activebackground='#2d3436', activeforeground="white")
        self.Z1.grid(row=1, column=0)
        self.Z1.grid(padx=15, pady=10)

        self.Z2 = tk.Button(root, text="Zone 2", width=10, height=5, bg='orange', fg="white",
                            activebackground='#2d3436', activeforeground="white")
        self.Z2.grid(row=1, column=1)
        self.Z2.grid(padx=15, pady=10)

        self.Z3 = tk.Button(root, text="Zone 3", width=10, height=5, bg='orange', fg="white",
                            activebackground='#2d3436', activeforeground="white")
        self.Z3.grid(row=2, column=0)
        self.Z3.grid(padx=15, pady=10)

        self.Z4 = tk.Button(root, text="Zone 4", width=10, height=5, bg='orange', fg="white",
                            activebackground='#2d3436', activeforeground="white")
        self.Z4.grid(row=2, column=1)
        self.Z4.grid(padx=15, pady=10)

        self.labelStatus = tk.Label(root, text="Status", borderwidth=2, font=('none', 15))
        self.labelStatus.grid(row=3, column=0, columnspan=2)
        self.labelStatus.grid(padx=5, pady=5)

        self.labelStatusRes = tk.Label(root, text="State", font=('none', 25))
        self.labelStatusRes.grid(row=4, column=0, columnspan=2)
        self.labelStatusRes.grid(padx=5, pady=5)
        self.labelStatusRes.config(bg='red')

        ################################################

        self.activate = tk.Button(root, text="Activate", width=15, height=2, fg="black",
                                  activebackground='#2d3436', activeforeground="white",
                                  command=self.arm
                                  )
        self.activate.grid(row=1, column=4)
        self.activate.grid(padx=15, pady=10)

        self.deactivate = tk.Button(root, text="Deactivate", width=15, height=2, fg="black",
                                    activebackground='#2d3436', activeforeground="white",
                                    command=self.disarm)
        self.deactivate.grid(row=2, column=4)
        self.deactivate.grid(padx=15, pady=10)

        self.reset = tk.Button(root, text="Reset", width=15, height=2, fg="black",
                               activebackground='#2d3436', activeforeground="white",
                               command=self.reset)
        self.reset.grid(row=3, column=4)
        self.reset.grid(padx=15, pady=10)

        #############################################################################

        self.alarm = tk.Entry(root)
        self.alarm.grid(row=4, column=4)

        self.btnAlarm = tk.Button(root, text="Declencher", command=self.setZone)
        self.btnAlarm.grid(row=5, column=4)

        self.resAlarm = tk.Label(root, text="OK")
        self.resAlarm.grid(row=5, column=0, columnspan=3)

    def allOn(self):
        self.labelStatusRes.config(text="on", bg='green')
        self.Z1.config(bg='green')
        self.Z2.config(bg='green')
        self.Z3.config(bg='green')
        self.Z4.config(bg='green')

    def allOff(self):
        self.labelStatusRes.config(text="off", bg='red')
        self.Z1.config(bg='orange')
        self.Z2.config(bg='orange')
        self.Z3.config(bg='orange')
        self.Z4.config(bg='orange')

    def reset(self):
        if self.SystemStatus:
            if self.AlarmStatus:
                self.labelStatusRes.config(text="on", bg='green')
                self.Z1.config(bg='green')
                self.Z2.config(bg='green')
                self.Z3.config(bg='green')
                self.Z4.config(bg='green')
                self.AlarmStatus = False
            else:
                self.resAlarm.config(text="Nothing to reset")
        else:
            self.resAlarm.config(text="You must activate alarm")

    def setZone(self):
        self.resAlarm.config(text="")
        if self.SystemStatus:
            val = self.alarm.get()
            if val == "1":
                self.Z1.config(bg='red')
            elif val == "2":
                self.Z2.config(bg='red')
            elif val == "3":
                self.Z3.config(bg='red')
            elif val == "4":
                self.Z4.config(bg='red')
            else:
                self.resAlarm.config(text="Zone undefined")
            self.AlarmStatus = True
            self.Led.on()
            self.Seg7.value = val
        else:
            self.resAlarm.config(text="Alarm desactivated")

    def arm(self):
        i = 1
        while i < 4:
            self.Led.on()
            self.Seg7.value = f"{i}"
            sleep(1)
            i += 1
        self.SystemStatus = True
        self.displayAndWait('A')
        self.allOn()

    def disarm(self):
        i = 3
        while i > 0:
            self.Led.on()
            self.Seg7.value = f"{i}"
            sleep(1)
            i -= 1

        self.SystemStatus = False
        self.displayAndWait('0')

        self.allOff()
        pass


f1 = tk.Tk()
app = tkForm(f1)
f1.mainloop()
