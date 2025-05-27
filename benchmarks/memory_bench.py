# benchmarks/memory_bench.py

import csv
import random

# Cache incluida directamente aquí para prueba autocontenida
class CacheLine:
    def __init__(self):
        self.valid = False
        self.tag = None
        self.data = None
        self.dirty = False

class Cache:
    def __init__(self, line_count=64, block_size=4, associativity=1):
        self.line_count = line_count
        self.block_size = block_size
        self.associativity = associativity
        self.sets = line_count // associativity
        self.cache = [[CacheLine() for _ in range(associativity)] for _ in range(self.sets)]

        self.hits = 0
        self.misses = 0
        self.writebacks = 0

    def _get_set_index_and_tag(self, address):
        block_addr = address // self.block_size
        set_index = block_addr % self.sets
        tag = block_addr // self.sets
        return set_index, tag

    def read(self, address):
        set_index, tag = self._get_set_index_and_tag(address)
        cache_set = self.cache[set_index]

        for line in cache_set:
            if line.valid and line.tag == tag:
                self.hits += 1
                return line.data

        self.misses += 1
        self._replace_line(cache_set, tag, read=True)
        return None

    def _replace_line(self, cache_set, tag, read=True, data=None):
        empty_line = next((line for line in cache_set if not line.valid), None)
        line = empty_line if empty_line else random.choice(cache_set)

        if line.valid and line.dirty:
            self.writebacks += 1

        line.valid = True
        line.tag = tag
        line.data = data if not read else None
        line.dirty = not read

    def stats(self):
        return {
            "hits": self.hits,
            "misses": self.misses,
            "writebacks": self.writebacks
        }

# --- Benchmark Principal ---
def benchmark_cache_access(cache, access_pattern, label):
    for addr in access_pattern:
        cache.read(addr)
    stats = cache.stats()
    print(f"\n[{label}]")
    print(f"Accesos: {len(access_pattern)}")
    print(f"Hits: {stats['hits']}, Misses: {stats['misses']}, Writebacks: {stats['writebacks']}")
    return {
        "tipo": label,
        "accesos": len(access_pattern),
        **stats
    }

def main():
    cache = Cache(line_count=64, block_size=4, associativity=1)

    sequential_accesses = [i * 4 for i in range(1000)]
    random_accesses = random.choices(sequential_accesses, k=1000)

    results = []
    results.append(benchmark_cache_access(cache, sequential_accesses, "Secuencial"))

    cache = Cache(line_count=64, block_size=4, associativity=1)
    results.append(benchmark_cache_access(cache, random_accesses, "Aleatorio"))

    with open("results_memory.csv", mode="w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["tipo", "accesos", "hits", "misses", "writebacks"])
        writer.writeheader()
        writer.writerows(results)

    print("\nResultados guardados en results_memory.csv")

if __name__ == "__main__":
    main()