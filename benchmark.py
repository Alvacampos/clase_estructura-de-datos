import random

from utils.utils import measure_time, measure_memory, generate_dummy_events, sequential_search, binary_search, bubble_sort, merge_sort, print_bench_table, divider
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

if __name__ == "__main__":
    runs = [100, 500, 1000]
    for _  in range(len(runs)):
        print(f"\nRun {_}:")
        # Generate a list of dummy events
        events = generate_dummy_events(runs[_])
        random.shuffle(events)  # Shuffle events to ensure they are not in sorted order
        comparative_table = []

        print("\nBenchmarking Binary Search:")
        binary_search_benchmark(events, runs[_])

        print("\nBenchmarking Sequential Search:")
        sequential_search_benchmark(events, runs[_])  # Searching for an event that does not exist to test worst-case scenario
        
        print("\nBenchmarking Bisect Search:")
        idx = bisect_search_benchmark(events, runs[_])  # Searching for an event that does not exist to test worst-case scenario
        divider()
        print("\nBenchmarking Bubble Sort:")
        bubble_sort_benchmark(events)

        print("\nBenchmarking Merge Sort:")
        merge_sort_benchmark(events)

        print("\nBased line sorted")
        based_line_sorted(events)

    print_bench_table()
