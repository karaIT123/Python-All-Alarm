import tkinter as tk
import gpiozero as gp
from time import sleep


class tkForm:
    char = gp.LEDCharDisplay(19, 26, 20, 16, 12, 13, 6, dp=21, active_high=False)
    led = gp.LED(18)
    button = gp.Button(23)
    button1 = gp.Button(25)
    button2 = gp.Button(22)
    button3 = gp.Button(27)
    button4 = gp.Button(17)
    systemStatus = False
    alarmStatus = False
    zn1 = False
    zn2 = False
    zn3 = False
    zn4 = False

    def __init__(self, root):
        self.Seg7 = tkForm.char
        self.Led = tkForm.led
        self.Button = tkForm.button
        self.Button1 = tkForm.button1
        self.Button2 = tkForm.button2
        self.Button3 = tkForm.button3
        self.Button4 = tkForm.button4
        self.AlarmStatus = tkForm.alarmStatus
        self.SystemStatus = tkForm.systemStatus
        self.zn1 = tkForm.zn1
        self.zn2 = tkForm.zn2
        self.zn3 = tkForm.zn3
        self.zn4 = tkForm.zn4

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

        # self.alarm = tk.Entry(root)
        # self.alarm.grid(row=4, column=4)
        #
        # self.btnAlarm = tk.Button(root, text="Declencher", command=self.setZone)
        # self.btnAlarm.grid(row=5, column=4)

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

    # def resetOne(self, val):
    #     #print("Reset")
    #     if val == "1":
    #         self.Z1.config(bg='green')
    #         #self.zn1 = False
    #     elif val == "2":
    #         self.Z2.config(bg='green')
    #         self.zn2 = False
    #     elif val == "3":
    #         self.Z3.config(bg='green')
    #         self.zn3 = False
    #     elif val == "4":
    #         self.Z4.config(bg='green')
    #         self.zn4 = False
    #     else:
    #         pass
    #     self.display("A")
    #     self.resAlarm.config(text="Zone undefined")

    def reset(self):
        if self.SystemStatus:
            if self.AlarmStatus:
                self.labelStatusRes.config(text="on", bg='green')
                self.Z1.config(bg='green')
                self.Z2.config(bg='green')
                self.Z3.config(bg='green')
                self.Z4.config(bg='green')
                self.AlarmStatus = False
                self.Seg7.value = "A"
            else:
                self.resAlarm.config(text="Nothing to reset")
        else:
            self.resAlarm.config(text="You must activate alarm")

    def setZone(self, val):
        self.resAlarm.config(text="")
        if self.SystemStatus:
            # val = self.alarm.get()
            if val == "1":
                self.Z1.config(bg='red')
                self.display(val)
                # self.zn1 = True
            elif val == "2":
                self.Z2.config(bg='red')
                self.display(val)
                # self.zn2 = True
            elif val == "3":
                self.Z3.config(bg='red')
                self.display(val)
                # self.zn3 = True
            elif val == "4":
                self.Z4.config(bg='red')
                self.display(val)
                # self.zn4 = True
            else:
                self.resAlarm.config(text="Zone undefined")
            self.AlarmStatus = True
            # self.Led.on()
            # self.Seg7.value = val
            # self.display(val)
        else:
            self.resAlarm.config(text="Alarm desactivated")

    def unsetZone(self, val):
        self.resAlarm.config(text="")
        if self.SystemStatus:
            # val = self.alarm.get()
            if val == "1":
                self.Z1.config(bg='green')
                self.display("A")
                # self.zn1 = True
            elif val == "2":
                self.Z2.config(bg='green')
                self.display("A")
                # self.zn2 = True
            elif val == "3":
                self.Z3.config(bg='green')
                self.display("A")
                # self.zn3 = True
            elif val == "4":
                self.Z4.config(bg='green')
                self.display("A")
                # self.zn4 = True
            else:
                self.resAlarm.config(text="Zone undefined")
            self.AlarmStatus = True
            # self.Led.on()
            # self.Seg7.value = val
            # self.display(val)
        else:
            self.resAlarm.config(text="Alarm desactivated")

    def display(self, val):
        self.Seg7.value = val
        # if self.Sec != "":
        #     #print('OK')
        #     self.resetOne(val)
        # else:
        #     self.Seg7.value = val
        #     self.Sec = val
        # self.Seg7.value = val

    def zone(self, val):
        if val == "1":
            if self.zn1:
                self.zn1 = False
                self.unsetZone(val)
                # print("unset")
            else:
                self.zn1 = True
                self.setZone(val)
                # print("set")
        elif val == "2":
            if self.zn2:
                self.zn2 = False
                self.unsetZone("2")
            else:
                self.zn2 = True
                self.setZone("2")
        elif val == "3":
            if self.zn3:
                self.zn3 = False
                self.unsetZone("3")
            else:
                self.zn3 = True
                self.setZone("3")
        elif val == "4":
            if self.zn4:
                self.zn4 = False
                self.unsetZone("4")
            else:
                self.zn4 = True
                self.setZone("4")
        else:
            pass

        # if self.zn3:
        #     self.resetOne("3")
        # else:
        #     self.setZone("3")
        #
        # if self.zn4:
        #     self.resetOne("4")
        # else:
        #     self.setZone("4")

    def setPersmission(self):
        self.Button1.when_pressed = lambda: self.zone("1")
        self.Button2.when_pressed = lambda: self.zone("2")
        self.Button3.when_pressed = lambda: self.zone("3")
        self.Button4.when_pressed = lambda: self.zone("4")

    def unsetPersmission(self):
        self.Button1.when_pressed = None
        self.Button2.when_pressed = None
        self.Button3.when_pressed = None
        self.Button4.when_pressed = None

    def arm(self):
        i = 1
        while i < 4:
            # self.Led.on()
            self.Seg7.value = f"{i}"
            sleep(1)
            i += 1
        self.SystemStatus = True
        self.Seg7.value = 'A'
        self.allOn()
        self.setPersmission()

    def disarm(self):
        i = 3
        while i > 0:
            # self.Led.on()
            self.Seg7.value = f"{i}"
            sleep(1)
            i -= 1

        self.SystemStatus = False
        self.Seg7.value = '0'

        self.allOff()
        self.unsetPersmission()
        pass


try:
    f1 = tk.Tk()
    app = tkForm(f1)
    f1.mainloop()
except KeyboardInterrupt:
    pass
