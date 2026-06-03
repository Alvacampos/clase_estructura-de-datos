"""
    This module contains the IncidentQueue class, which is responsible for managing a queue of incidents.
"""
from collections import deque

class IncidentQueue:
    """
        A simple queue implementation for managing incidents. Incidents are added to the end of the queue and retrieved from the front, following a first-in-first-out (FIFO) order.
        The IncidentQueue class provides methods to add incidents, retrieve the next incident, and check if the queue is empty.
        The 'queue' variable is a deque (double-ended queue) from the collections module, which allows for efficient appending and popping of items from both ends of the queue.
    """
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        """
            BigO: O(1) for checking if the queue is empty, as it simply checks if the deque is empty.
        """
        return len(self.queue) == 0

    def add_incident(self, incident):
        """
            BigO: O(1) for adding an incident to the queue, as it simply appends the incident to the end of the deque.
        """
        self.queue.append(incident)

    def get_next_incident(self):
        """
            BigO: O(1) for retrieving the next incident from the queue, as it removes and returns the incident from the front of the deque.
        """
        try:
            return self.queue.popleft()
        except IndexError:
            return None
    
    def size(self):
        """
            BigO: O(1) for getting the size of the queue, as it simply returns the length of the deque.
        """
        return len(self.queue)