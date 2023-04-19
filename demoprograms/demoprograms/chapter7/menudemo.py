"""
File: menudemo.py
Author: Kenneth A. Lambert
"""

from breezypythongui import EasyFrame
from order import Order

class MenuDemo(EasyFrame):
    """Allows the user to place a restaurant order from a set
    of options."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Menu Demo")

        # Create the model
        self.order = Order()
        
        # Add the menu bar for the three menus
        menuBar = self.addMenuBar(row = 0, column = 0)
        
        # Add the Meat menu and its options
        meatMenu = menuBar.addMenu("Meat")
        meatMenu.addMenuItem("Beef",
                             lambda : self.order.set("Meat", "Beef"))
        meatMenu.addMenuItem("Chicken",
                             lambda : self.order.set("Meat", "Chicken"))
        meatMenu.addMenuItem("Fish",
                         lambda : self.order.set("Meat", "Fish"))
        
        # Add the Potato menu and its options
        taterMenu = menuBar.addMenu("Potato")
        taterMenu.addMenuItem("French fries",
                              lambda : self.order.set("Potato",
                                                      "French fries"))
        taterMenu.addMenuItem("Baked potato",
                              lambda : self.order.set("Potato",
                                                      "Baked potato"))
        taterMenu.addMenuItem("Scalloped potato",
                              lambda : self.order.set("Potato",
                                                      "Scalloped potato"))
        
        # Add the Vegetable menu and its options
        vegMenu = menuBar.addMenu("Vegetable")
        vegMenu.addMenuItem("Green beans",
                            lambda : self.order.set("Vegetable",
                                                    "Green Beans"))
        vegMenu.addMenuItem("Broccoli",
                            lambda : self.order.set("Vegetable",
                                                    "Broccoli"))
        vegMenu.addMenuItem("Applesauce",
                            lambda : self.order.set("Vegetable",
                                                    "Applesauce"))

        # Add the command button
        self.addButton(text = "Place order", row = 1, column = 0,
                       columnspan = 3, command = self.placeOrder)
        
    # Event handling method
    def placeOrder(self):
        """Display a message box with the order information."""
        message = str(self.order)
        if message == "": message = "No food ordered!"
        self.messageBox(title = "Customer Order", message = message)

# Instantiate and pop up the window."""
if __name__ == "__main__":
    MenuDemo().mainloop()
