import random

from queues.priority_queue import PriorityQueue
from queues.incident_queue import IncidentQueue
from router.router import Router
from storage.event_store import EventStore
from graphs.graph import Graph
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

    divider()
    print('Router Test:')
    # Create an instance of the Router and add some routes
    router = Router()
    for event in events:
        router.add_route(event.origin, event.destination)

    router.add_route("Backup-A", "Backup-B")
    router.add_route("Backup-C", "Backup-D")

    print(f'Amount of zones: {router.zone_count()}')
    print(f'Amount of connected zones: {router.zone_count()}')
    print(f'System 0 ↔ System 50: {router.are_connected("System 0", "System 50")}')
    print(f'System 0 ↔ Backup-A: {router.are_connected("System 0", "Backup-A")}')
    print(f'Backup-A ↔ Backup-B: {router.are_connected("Backup-A", "Backup-B")}')     # True
    print(f'Backup-A ↔ Backup-C: {router.are_connected("Backup-A", "Backup-C")}')

    divider()
    print('Graph algorithms (BFS, DFS, Dijkstra, MST):')
    random.seed(42)
    g = Graph()
    for event in events[:20]:
        g.add_edge(event.origin, event.destination, weight=random.randint(1, 100))
    print(f'  Nodes: {g.num_nodes()}, Edges: {g.num_edges()}')
    print('  BFS from "System 0":', g.bfs("System 0")[:8], '...')
    print('  DFS from "System 0":', g.dfs("System 0")[:8], '...')
    distances = g.shortest_distances("System 0")
    print(f'  Dijkstra: distance to "System 10" = {distances.get("System 10")}')
    mst = g.minimum_spanning_tree()
    print(f'  MST: {len(mst)} edges, total weight = {sum(w for _, _, w in mst)}')


if __name__ == "__main__":
    main()
