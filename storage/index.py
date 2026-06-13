"""
This module contains the Index class, an in-memory index by event id
that allows O(1) average-time lookup using Python's built-in dict.
"""


class Index:
    """
    Hash-based index that maps event id → Event.

    Average-case complexity for add, remove and
    search is O(1).
    """

    def __init__(self):
        self._index = {}

    def add(self, event):
        """Register an event in the index. O(1) average."""
        self._index[event.id] = event

    def remove(self, event_id):
        """Remove an event from the index by its id. O(1) average."""
        self._index.pop(event_id, None)

    def search(self, event_id):
        """Return the event with the given id, or None if not present. O(1) average."""
        return self._index.get(event_id)

    def size(self):
        """O(1)."""
        return len(self._index)

    def all(self):
        """Return all indexed events. O(n)."""
        return list(self._index.values())
