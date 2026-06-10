from models.event import Event
from queues.priority_queue import PriorityQueue
from queues.incident_queue import IncidentQueue 
from utils.utils import divider


def main():
    divider()
    print('Dummy Events:')
    # Create some dummy events
    event1 = Event(1, "2024-06-01T12:00:00Z", "Network", 1, "Network outage in building A", "System A", "System B")
    event2 = Event(2, "2024-06-01T12:05:00Z", "Hardware", 2, "Server overheating in data center", "System C", "System D")
    event3 = Event(3, "2024-06-01T12:10:00Z", "Software", 3, "Application crash on user device", "System E", "System F")
    event1.print_event()
    event2.print_event()
    event3.print_event()
    divider()

    # Create an instance of the PriorityQueue
    priority_queue = PriorityQueue()
    
    # Add some items to the priority queue with different priorities
    priority_queue.add(event1, event1.priority)  # High priority
    priority_queue.add(event2, event2.priority)  # Medium priority
    priority_queue.add(event3, event3.priority)  # Low priority


    print('Priority Queue:')
    # Retrieve items from the priority queue based on their priority
    print(priority_queue.pop())  # Output: "High priority task"
    print(priority_queue.pop())  # Output: "Medium priority task"
    print(priority_queue.pop())  # Output: "Low priority task"

    # Create an instance of the IncidentQueue
    incident_queue = IncidentQueue()
    
    # Add some incidents to the incident queue
    incident_queue.add_incident(event3.text)
    incident_queue.add_incident(event1.text)
    incident_queue.add_incident(event2.text)

    divider()
    print('Incident Queue:')
    # Retrieve incidents from the incident queue in FIFO order
    print('-', incident_queue.get_next_incident())  # Output: "Incident 1"
    print('-', incident_queue.get_next_incident())  # Output: "Incident 2"
    print('-', incident_queue.get_next_incident())  # Output: "Incident 3"

if __name__ == "__main__":
    main()