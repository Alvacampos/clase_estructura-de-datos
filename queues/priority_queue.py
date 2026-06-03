"""
    This module contains the PriorityQueue class, which is responsible for managing a priority queue.
    The PriorityQueue class provides methods to add items with a specified priority, retrieve the next item based on priority, peek at the next item without removing it, and check if the queue is empty or get its size.
"""
import heapq

class PriorityQueue:
    """
        A priority queue implementation using a heap. Items are stored as tuples of (priority, count, item) to ensure that items with the same priority are returned in the order they were added.
        The 'counter' variable is used to maintain the order of items with the same priority.
    """
    def __init__(self):
        self.pq = []
        self.counter = 0

    def is_empty(self):
        """
            BigO: O(1) for checking if the priority queue is empty, as it simply checks if the list of elements is empty. 
        """
        return not self.pq
    
    def add(self, item, priority):
        """
            BigO: O(log n) for adding an item to the priority queue, where n is the number of items in the queue. This is because the heapq.heappush operation maintains the heap property after adding a new item.
        """
        heapq.heappush(self.pq, (priority, self.counter, item))
        self.counter += 1

    def pop(self):
        """
            BigO: O(log n) for retrieving the next item from the priority queue, where n is the number of items in the queue. This is because the heapq.heappop operation maintains the heap property after removing the item with the highest priority.
        """
        try:
            return heapq.heappop(self.pq)[2]
        except IndexError:
            return None

    def peek(self):
        """
            BigO: O(1) for peeking at the next item in the priority queue, as it simply returns the first item in the list of elements.
        """
        try:
            return self.pq[0][2]
        except IndexError:
            return None

    def size(self):
        """
            BigO: O(1) for getting the size of the priority queue, as it simply returns the length of the list of elements.
        """
        return len(self.pq)