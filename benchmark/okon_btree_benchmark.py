import random
import subprocess
import sys
import os


OKON_CALLER = sys.argv[1]
NUMBER_OF_HASHED_TO_BENCHMARK = int(sys.argv[2])
PATH_TO_ORIGINAL_FILE = sys.argv[3]
NUMBER_OF_HASHES_IN_ORIGINAL_FILE = int(sys.argv[4])
BTREE_FILE_TO_BENCHMARK = sys.argv[5]
BENCHMARK_SEED = sys.argv[6] if len(sys.argv) > 6 else 0

def generate_hashes_indices():
    random.seed(BENCHMARK_SEED)

    indices = []
    for _ in range(NUMBER_OF_HASHED_TO_BENCHMARK):
        indices.append(random.randint(0, NUMBER_OF_HASHES_IN_ORIGINAL_FILE - 1))

    indices.sort()
    return indices


def collect_hashes_to_benchmark():
    indices = generate_hashes_indices()
    print('Indices to get: ' + str(indices))
    hashes = []

    counter = 0
    index_no = 0

    with open(PATH_TO_ORIGINAL_FILE, 'r') as original_file:
        while index_no < len(indices):
            line = original_file.readline()

            if counter == indices[index_no]:
                print('[{}/{}] Got [{}]: {}'.format(index_no, len(indices), indices[index_no], line[:40]))
                hashes.append(line[:40])
                index_no += 1

            counter += 1

    return hashes


def run_benchmark(hash_to_benchmark):
    os.system('sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"')
    command = [OKON_CALLER, hash_to_benchmark, BTREE_FILE_TO_BENCHMARK]
    return subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8')


def run_benchmarks(hashes):
    results = []

    counter = 0

    for h in hashes:
        output = run_benchmark(h)
        results.append(int(output))
        print('[{}/{}] Benchmarking {}'.format(counter, len(hashes), h))
        counter += 1

    return results

hashes = collect_hashes_to_benchmark()
results = run_benchmarks(hashes)

print('Benchmark done, result: {}'.format(sum(results) / len(results)))
