import bisect
import random

from analisys.text_analyzer import TextAnalyzer
from graphs.graph import Graph
from utils.utils import (
    binary_search,
    bubble_sort,
    divider,
    generate_dummy_events,
    measure_memory,
    measure_time,
    merge_sort,
    print_bench_table,
    reset_bench_table,
    sequential_search,
)


@measure_memory
@measure_time
def binary_search_benchmark(events, target):
    sorted_events = sorted(events, key=lambda e: e.id)
    index = binary_search(sorted_events, target, key=lambda e: e.id)
    return index


@measure_memory
@measure_time
def sequential_search_benchmark(events, target):
    index = sequential_search(events, target)
    return index


@measure_memory
@measure_time
def bisect_search_benchmark(events, target):
    sorted_events = sorted(events, key=lambda e: e.id)
    index = bisect.bisect_left(sorted_events, target, key=lambda e: e.id)
    return index


@measure_memory
@measure_time
def bubble_sort_benchmark(events):
    sorted_events = bubble_sort(events, key=lambda e: e.id)
    return sorted_events


@measure_memory
@measure_time
def merge_sort_benchmark(events):
    sorted_events = merge_sort(events, key=lambda e: e.id)
    return sorted_events


@measure_memory
@measure_time
def based_line_sorted(events):
    sorted_events = sorted(events, key=lambda e: e.id)
    return sorted_events


def build_graph_from_events(events):
    """Build a weighted undirected graph from events. Random weights for Dijkstra/MST."""
    rng = random.Random(42)
    g = Graph()
    for event in events:
        g.add_edge(event.origin, event.destination, weight=rng.randint(1, 100))
    return g


@measure_memory
@measure_time
def bfs_benchmark(graph_nodes, start):
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


@measure_memory
@measure_time
def brute_force_search_benchmark(text, pattern):
    ta = TextAnalyzer()
    return ta.brute_force_search(text, pattern)


@measure_memory
@measure_time
def kmp_search_benchmark(text, pattern):
    ta = TextAnalyzer()
    return ta.kmp_search(text, pattern)


def build_pathological_text(n, char='a'):
    """
    Build a worst-case text for brute-force pattern matching.
    Repeats `char` n-1 times, ends with 'b'. Combined with a similar
    pattern this forces brute-force to backtrack heavily.
    """
    return char * (n - 1) + 'b'


if __name__ == "__main__":
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

    print("\n")
    print("=" * 60)
    print("PART 2 — Pattern search benchmarks (Brute force vs KMP)")
    print("=" * 60)
    reset_bench_table()

    text_sizes = [1000, 10000, 50000]
    for size in text_sizes:
        print(f"\nRun (text length {size}):")
        text = build_pathological_text(size)
        pattern = 'a' * 50 + 'b'

        print("\nBenchmarking Brute Force Search:")
        brute_force_search_benchmark(text, pattern)

        print("\nBenchmarking KMP Search:")
        kmp_search_benchmark(text, pattern)

    print_bench_table()
