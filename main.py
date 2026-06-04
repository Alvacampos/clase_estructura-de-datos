from queues.priority_queue import PriorityQueue
from queues.incident_queue import IncidentQueue 
from storage.event_store import EventStore
from utils.utils import divider, generate_dummy_events


def main():
    divider()
    print('Dummy Events:')
    # Create some dummy events
    events = generate_dummy_events(100)
    divider()

    # Create an instance of the PriorityQueue
    priority_queue = PriorityQueue()
    
    # Add some items to the priority queue with different priorities
    for event in events[:10]:  # Add first 10 events for demonstration
        priority_queue.add(event, event.priority)


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
    
    divider()
    print('Event Store Test:')
    event_store = EventStore()
    for event in events:
        event_store.add_event(event)

    # Test searching for events by ID
    found_event = event_store.search_by_id(events[75].id)
    if found_event:
        print(f'Found event: {found_event.text}')
    else:
        print('Event not found.')

if __name__ == "__main__":
    main()