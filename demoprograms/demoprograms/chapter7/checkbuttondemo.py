"""
File: checkbuttondemo.py
Author: Kenneth A. Lambert
"""

from breezypythongui import EasyFrame

class CheckbuttonDemo(EasyFrame):
    """Allows the user to place a restaurant order from a set
    of options."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Check Button Demo")
        
        # Add four check buttons
        self.chickCB = self.addCheckbutton(text = "Chicken",
                                           row = 0, column = 0)

        self.taterCB = self.addCheckbutton(text = "French fries",
                                           row = 0, column = 1)

        self.beanCB = self.addCheckbutton(text = "Green beans",
                                          row = 1, column = 0)
        
        self.sauceCB = self.addCheckbutton(text = "Applesauce",
                                           row = 1, column = 1)

        self.addButton(text = "Place order", row = 2, column = 0,
                       columnspan = 2, command = self.placeOrder)
        
    # Event handler method

    def placeOrder(self):
        """Display a message box with the order information."""
        message = ""
        if self.chickCB.isChecked():
            message += "Chicken\n\n"
        if self.taterCB.isChecked():
            message += "French fries\n\n"
        if self.beanCB.isChecked():
            message += "Green beans\n\n"
        if self.sauceCB.isChecked():
            message += "Applesauce\n"
        if message == "": message = "No food ordered!"
        self.messageBox(title = "Customer Order", message = message)
                

# Instantiate and pop up the window."""
if __name__ == "__main__":
    CheckbuttonDemo().mainloop()
