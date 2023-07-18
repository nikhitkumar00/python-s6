from breezypythongui import EasyFrame


class Counter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Counter")

        self.addLabel(text="Count", row=0, column=0, sticky="NSEW")
        self.Number = self.addIntegerField(value=0, row=1, column=0, sticky="NSEW")

        self.addButton(text="Inc", row=2, column=0, command=self.increment)
        self.addButton(text="Dec", row=3, column=0, command=self.decrement)

    def increment(self):
        c = self.Number.getNumber()
        dgt = c + 1
        self.Number.setNumber(dgt)

    def decrement(self):
        c = self.Number.getNumber()
        dgt = c - 1
        self.Number.setNumber(dgt)


Counter().mainloop()
