from breezypythongui import EasyFrame

class SimpleGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Simple GUI",width=500,height=200)
        self["background"] = "black"
        self.text = self.addLabel(text="Hello, GUI!", row=0, column=0)
        self.addButton(text="Click Me", row=1, column=0, command=self.on_button_click)

    def on_button_click(self):
        self.text["text"] = "Button clicked!"

if __name__ == "__main__":
    SimpleGUI().mainloop()