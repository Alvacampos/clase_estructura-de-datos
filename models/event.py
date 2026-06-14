"""
    This module contains the Event class, which represents an event in the system.
"""


class Event:
    def __init__(self, id, timestamp, category, priority, text, origin, destination):
        self.id = id
        self.timestamp = timestamp
        self.category = category
        self.priority = priority
        self.text = text
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return f"Event(id={self.id}, timestamp={self.timestamp}, category={self.category}, priority={self.priority}, text={self.text}, origin={self.origin}, destination={self.destination})"

    def print_event(self):
        print(self.__str__())
