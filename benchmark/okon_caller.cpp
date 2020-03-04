#include <benchmark/benchmark.h>

#include <btree.hpp>
#include <fstream_wrapper.hpp>

#include <chrono>

#include <iostream>

int main(int argc, const char* argv[])
{
  const auto benchmark_hash = argv[1];
  const auto benchmark_btree_file = argv[2];

  typedef std::chrono::high_resolution_clock Time;
  typedef std::chrono::microseconds micros;

  const auto start = Time::now();

  okon::fstream_wrapper wrapper{ benchmark_btree_file };
  okon::btree<okon::fstream_wrapper> tree{ wrapper };
  const auto result = tree.contains(okon::string_sha1_to_binary(benchmark_hash));

  const auto end = Time::now();

  const auto duration_micros = std::chrono::duration_cast<micros>(end - start);
  std::cout << duration_micros.count() << '\n';

  benchmark::DoNotOptimize(result);

  return 0;
}
