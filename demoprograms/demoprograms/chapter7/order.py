"""
File: order.py
Author: Kenneth A. Lambert
"""

class Order(object):
    """Models a customer order at a restaurant."""

    def __init__(self):
        """Sets up the model."""
        self._items = {}

    def set(self, itemType, value):
        """Inserts the value of the item type."""
        self._items[itemType] = value
        return value

    def __str__(self):
        """Returns the string rep of the order."""
        return "\n\n".join(self._items.values())
