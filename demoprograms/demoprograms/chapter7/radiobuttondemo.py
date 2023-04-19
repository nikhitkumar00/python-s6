"""
File: radiobuttondemo.py
Author: Kenneth A. Lambert
"""

from breezypythongui import EasyFrame

class RadiobuttonDemo(EasyFrame):
    """Allows the user to place a restaurant order from a set
    of options."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Radio Button Demo")

        # Add the label, button group, and buttons for meats
        self.addLabel(text = "Meat", row = 0, column = 0)
        self.meatGroup = self.addRadiobuttonGroup(row = 1,
                                                  column = 0,
                                                  rowspan = 2)
        defaultRB = self.meatGroup.addRadiobutton(text = "Chicken")
        self.meatGroup.setSelectedButton(defaultRB)
        self.meatGroup.addRadiobutton(text = "Beef")

        # Add the label, button group, and buttons for potatoes
        self.addLabel(text = "Potato", row = 0, column = 1)
        self.taterGroup = self.addRadiobuttonGroup(row = 1,
                                                   column = 1,
                                                   rowspan = 2)
        defaultRB = self.taterGroup.addRadiobutton(text = "French fries")
        self.taterGroup.setSelectedButton(defaultRB)
        self.taterGroup.addRadiobutton(text = "Baked potato")

        # Add the label, button group, and buttons for veggies
        self.addLabel(text = "Vegetable", row = 0, column = 2)
        self.vegGroup = self.addRadiobuttonGroup(row = 1,
                                                  column = 2,
                                                  rowspan = 2)
        defaultRB = self.vegGroup.addRadiobutton(text = "Applesauce")
        self.vegGroup.setSelectedButton(defaultRB)
        self.vegGroup.addRadiobutton(text = "Green beans")

        self.addButton(text = "Place order", row = 3, column = 0,
                       columnspan = 3, command = self.placeOrder)
        
    # Event handler method

    def placeOrder(self):
        """Display a message box with the order information."""
        message = ""
        message += self.meatGroup.getSelectedButton()["text"] + "\n\n"
        message += self.taterGroup.getSelectedButton()["text"] + "\n\n"
        message += self.vegGroup.getSelectedButton()["text"]
        self.messageBox(title = "Customer Order", message = message)
                

# Instantiate and pop up the window."""
if __name__ == "__main__":
    RadiobuttonDemo().mainloop()
