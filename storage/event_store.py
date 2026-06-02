"""
    This module contains the EventStore class, which is responsible for storing events in memory.
"""
class EventStore:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        
    def delete_event(self, event_id):
        self.events = [event for event in self.events if event.id != event_id]

    def get_events(self):
        return self.events