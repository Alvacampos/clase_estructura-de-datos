from models.event import Event
from queues.priority_queue import PriorityQueue
from queues.incident_queue import IncidentQueue 
from utils.utils import divider, generate_dummy_events


def main():
    divider()
    print('Dummy Events:')
    # Create some dummy events
    events = generate_dummy_events(3)
    events[0].print_event()
    events[1].print_event()
    events[2].print_event()
    divider()

    # Create an instance of the PriorityQueue
    priority_queue = PriorityQueue()
    
    # Add some items to the priority queue with different priorities
    priority_queue.add(events[0], events[0].priority)  # High priority
    priority_queue.add(events[1], events[1].priority)  # Medium priority
    priority_queue.add(events[2], events[2].priority)  # Low priority


    print('Priority Queue:')
    # Retrieve items from the priority queue based on their priority
    print(priority_queue.pop())  # Output: "High priority task"
    print(priority_queue.pop())  # Output: "Medium priority task"
    print(priority_queue.pop())  # Output: "Low priority task"

    # Create an instance of the IncidentQueue
    incident_queue = IncidentQueue()
    
    # Add some incidents to the incident queue
    incident_queue.add_incident(events[2].text)
    incident_queue.add_incident(events[0].text)
    incident_queue.add_incident(events[1].text)

    divider()
    print('Incident Queue:')
    # Retrieve incidents from the incident queue in FIFO order
    print('-', incident_queue.get_next_incident())  # Output: "Incident 1"
    print('-', incident_queue.get_next_incident())  # Output: "Incident 2"
    print('-', incident_queue.get_next_incident())  # Output: "Incident 3"

if __name__ == "__main__":
    main()