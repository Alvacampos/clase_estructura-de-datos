import random

from crypto.rsa import RSA
from graphs.graph import Graph
from queues.incident_queue import IncidentQueue
from queues.priority_queue import PriorityQueue
from router.router import Router
from storage.event_store import EventStore
from utils.utils import divider, generate_dummy_events


def main():
    events = generate_dummy_events(100)

    divider()
    print('Priority Queue:')
    priority_queue = PriorityQueue()
    for event in events[:10]:
        priority_queue.add(event, event.priority)
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())

    divider()
    print('Incident Queue:')
    incident_queue = IncidentQueue()
    incident_queue.add_incident(events[2].text)
    incident_queue.add_incident(events[0].text)
    incident_queue.add_incident(events[1].text)
    print('-', incident_queue.get_next_incident())
    print('-', incident_queue.get_next_incident())
    print('-', incident_queue.get_next_incident())

    divider()
    print('Event Store Test:')
    event_store = EventStore()
    for event in events:
        event_store.add_event(event)
    found_event = event_store.search_by_id(events[75].id)
    if found_event:
        print(f'Found event: {found_event.text}')
    else:
        print('Event not found.')

    divider()
    print('Router Test (Union-Find):')
    router = Router()
    for event in events:
        router.add_route(event.origin, event.destination)
    router.add_route("Backup-A", "Backup-B")
    router.add_route("Backup-C", "Backup-D")
    print(f'  Connected zones: {router.zone_count()}')
    print(f'  System 0 ↔ System 50: {router.are_connected("System 0", "System 50")}')
    print(f'  System 0 ↔ Backup-A:  {router.are_connected("System 0", "Backup-A")}')
    print(f'  Backup-A ↔ Backup-B:  {router.are_connected("Backup-A", "Backup-B")}')
    print(f'  Backup-A ↔ Backup-C:  {router.are_connected("Backup-A", "Backup-C")}')

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

    divider()
    print('RSA Test:')
    rsa = RSA(p=61, q=53)
    print(f'  Public key  (n, e): {rsa.public_key()}')
    print(f'  Private key (n, d): {rsa.private_key()}')

    m = 42
    c = rsa.encrypt(m)
    print(f'  Encrypt int {m} -> {c}; decrypt -> {rsa.decrypt(c)}')

    payload = "incidente-A:42"
    encrypted = rsa.encrypt(payload)
    print(f'  Encrypt "{payload}" -> {encrypted[:4]}... ({len(encrypted)} ints)')
    print(f'  Decrypt -> "{rsa.decrypt(encrypted)}"')


if __name__ == "__main__":
    main()
