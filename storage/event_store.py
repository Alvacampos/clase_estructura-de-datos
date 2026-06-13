"""
    This module contains the EventStore class, which is responsible for storing events in memory.
"""

from storage.index import Index


class EventStore:
    """Simple in-memory event store that uses an Index for O(1) average-time lookup by event id."""
    def __init__(self):
        self._index = Index()
        self.events = []

    def add_event(self, event):
        """Add an event to the store and index it. O(1) average."""
        self._index.add(event)
        self.events.append(event)

    def delete_event(self, event_id):
        """Delete an event from the store and remove it from the index. O(1) average."""
        self._index.remove(event_id)
        self.events = [event for event in self.events if event.id != event_id]

    def get_events(self):
        """Return all events. O(n)."""
        return self._index.all()

    def search_by_id(self, event_id):
        """Return event by id using the index. O(1) average."""
        return self._index.search(event_id)