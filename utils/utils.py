import timeit
import tracemalloc
from functools import wraps

from models.event import Event

_bench_data = []


def divider():
    print("-" * 50)


def get_bench_table():
    """Return the accumulated benchmark data."""
    return _bench_data


def reset_bench_table():
    """Clear all benchmark data."""
    _bench_data.clear()


def print_bench_table():
    """Print the accumulated benchmark data as a comparative table.

    Rows: input size n.
    Columns: one pair (time, memory_peak) per benchmarked function.
    """
    if not _bench_data:
        print("(bench table is empty)")
        return

    lookup = {}
    sizes = set()
    funcs = []
    for entry in _bench_data:
        func = entry["func"]
        if func not in lookup:
            lookup[func] = {}
            funcs.append(func)
        n = entry["n"]
        sizes.add(n)
        lookup[func].setdefault(n, {})[entry["metric"]] = entry["value"]

    sizes = sorted(sizes, key=lambda x: (x is None, x))

    name_w = 12
    print()
    print("=" * (10 + len(funcs) * (name_w * 2 + 3)))
    print(f"{'n':>8}  " + "  ".join(f"{f[:name_w*2+1]:<{name_w*2+1}}" for f in funcs))
    print(f"{'':>8}  " + "  ".join(
        f"{'time(s)':<{name_w}} {'mem(MB)':<{name_w}}" for _ in funcs
    ))
    print("-" * (10 + len(funcs) * (name_w * 2 + 3)))

    for n in sizes:
        row = f"{str(n):>8}  "
        cells = []
        for func in funcs:
            t = lookup[func].get(n, {}).get("time")
            m = lookup[func].get(n, {}).get("memory_peak")
            t_str = f"{t:.6f}" if t is not None else "-"
            m_str = f"{m:.6f}" if m is not None else "-"
            cells.append(f"{t_str:<{name_w}} {m_str:<{name_w}}")
        print(row + "  ".join(cells))
    print("=" * (10 + len(funcs) * (name_w * 2 + 3)))


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - start
        print(f"Execution time: {elapsed:.6f} seconds")
        n = len(args[0]) if args else None
        _bench_data.append({
            "func": func.__name__,
            "metric": "time",
            "value": elapsed,
            "n": n
        })
        return result
    return wrapper


def measure_memory(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 10**6:.6f} MB; Peak memory usage: {peak / 10**6:.6f} MB")
        tracemalloc.stop()
        n = len(args[0]) if args else None
        _bench_data.append({
            "func": func.__name__,
            "metric": "memory_peak",
            "value": peak / 10**6,
            "n": n
        })
        return result
    return wrapper


def generate_dummy_events(num_events):
    events = []
    for i in range(num_events):
        event = Event(i, f"2024-06-01T12:{i:02d}:00Z", "Category", i % 5, f"Event {i}", f"System {i}", f"System {i+1}")
        events.append(event)
    return events

def binary_search(arr, target, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_key = key(arr[mid])
        if mid_key == target:
            return mid
        elif mid_key < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(arr[j]) > key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, key)
        merge_sort(R, key)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if key(L[i]) < key(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr