import random

from utils.utils import measure_time, measure_memory, generate_dummy_events, sequential_search, binary_search, bubble_sort, merge_sort, print_bench_table, divider, reset_bench_table
from graphs.graph import Graph
import bisect

@measure_memory
@measure_time
def binary_search_benchmark(events, target):
    # Sort events by priority to use binary search
    sorted_events = sorted(events, key=lambda e: e.id)
    # Perform binary search
    index = binary_search(sorted_events, target, key=lambda e: e.id)

    return index

@measure_memory
@measure_time
def sequential_search_benchmark(events, target):
    # Perform sequential search for the target event
    index = sequential_search(events, target)

    return index

@measure_memory
@measure_time
def bisect_search_benchmark(events, target):
    # Sort events by priority to use bisect
    sorted_events = sorted(events, key=lambda e: e.id)
    # Perform binary search using bisect
    index = bisect.bisect_left(sorted_events, target, key=lambda e: e.id)

    return index


@measure_memory
@measure_time
def bubble_sort_benchmark(events):
    # Sort events using bubble sort
    sorted_events = bubble_sort(events, key=lambda e: e.id)

    return sorted_events


@measure_memory
@measure_time
def merge_sort_benchmark(events):
    # Sort events using merge sort
    sorted_events = merge_sort(events, key=lambda e: e.id)

    return sorted_events

@measure_memory
@measure_time
def based_line_sorted(events):
    # Sort events using Python's built-in sorted function
    sorted_events = sorted(events, key=lambda e: e.id)

    return sorted_events


def build_graph_from_events(events):
    """Build a weighted undirected graph from events. Random weights for Dijkstra/MST."""
    rng = random.Random(42)  # deterministic
    g = Graph()
    for event in events:
        g.add_edge(event.origin, event.destination, weight=rng.randint(1, 100))
    return g


@measure_memory
@measure_time
def bfs_benchmark(graph_nodes, start):
    # graph_nodes is a Graph; argument named so measure_* can read len()
    return graph_nodes.bfs(start)


@measure_memory
@measure_time
def dfs_benchmark(graph_nodes, start):
    return graph_nodes.dfs(start)


@measure_memory
@measure_time
def dijkstra_benchmark(graph_nodes, start):
    return graph_nodes.shortest_distances(start)


@measure_memory
@measure_time
def kruskal_benchmark(graph_nodes):
    return graph_nodes.minimum_spanning_tree()


if __name__ == "__main__":
    # =========================================================
    # Part 1 — search and sort benchmarks
    # =========================================================
    print("=" * 60)
    print("PART 1 — Search and Sort benchmarks")
    print("=" * 60)
    runs = [100, 500, 1000]
    for _ in range(len(runs)):
        print(f"\nRun {_}:")
        events = generate_dummy_events(runs[_])
        random.shuffle(events)

        print("\nBenchmarking Binary Search:")
        binary_search_benchmark(events, runs[_])

        print("\nBenchmarking Sequential Search:")
        sequential_search_benchmark(events, runs[_])

        print("\nBenchmarking Bisect Search:")
        idx = bisect_search_benchmark(events, runs[_])
        divider()
        print("\nBenchmarking Bubble Sort:")
        bubble_sort_benchmark(events)

        print("\nBenchmarking Merge Sort:")
        merge_sort_benchmark(events)

        print("\nBaseline sorted (Timsort)")
        based_line_sorted(events)

    print_bench_table()

    # =========================================================
    # Part 2 — graph algorithm benchmarks
    # =========================================================
    print("\n")
    print("=" * 60)
    print("PART 2 — Graph algorithms benchmarks (BFS, DFS, Dijkstra, Kruskal)")
    print("=" * 60)
    reset_bench_table()

    graph_sizes = [50, 200, 500]
    for size in graph_sizes:
        print(f"\nRun (graph with {size} edges):")
        events = generate_dummy_events(size)
        g = build_graph_from_events(events)
        start_node = events[0].origin

        print("\nBenchmarking BFS:")
        bfs_benchmark(g, start_node)

        print("\nBenchmarking DFS:")
        dfs_benchmark(g, start_node)

        print("\nBenchmarking Dijkstra:")
        dijkstra_benchmark(g, start_node)

        print("\nBenchmarking Kruskal MST:")
        kruskal_benchmark(g)

    print_bench_table()
