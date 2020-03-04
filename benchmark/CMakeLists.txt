add_executable(okon_benchmarks
    exists_benchmark.cpp
)

if(NOT OKON_BENCHMARK_FILE)
    message(FATAL_ERROR "Set OKON_BENCHMARK_PREPARED_DIR variable and try again")
endif()

if(NOT OKON_BENCHMARK_PREPARED_DIR)
    message(FATAL_ERROR "Set OKON_BENCHMARK_PREPARED_DIR variable and try again")
endif()

target_include_directories(okon_benchmarks
    PRIVATE
        ${OKON_DIR}
        ${benchmark_INCLUDE_DIRS}
)

target_link_libraries(okon_benchmarks
    PRIVATE
        okon
        ${benchmark_LIBRARIES}
        ${CMAKE_THREAD_LIBS_INIT}
)

target_compile_definitions(okon_benchmarks
    PRIVATE
        -DOKON_BENCHMARK_FILE="${OKON_BENCHMARK_FILE}"
        -DOKON_BENCHMARK_BEST_CASE="${OKON_BENCHMARK_BEST_CASE}"
        -DOKON_BENCHMARK_WORST_CASE="${OKON_BENCHMARK_WORST_CASE}"
        -DOKON_BENCHMARK_BTREE_FILE="${OKON_BENCHMARK_BTREE_FILE}"
)

add_executable(okon_caller okon_caller.cpp)
target_include_directories(okon_caller
    PRIVATE
        ${OKON_DIR}
        ${benchmark_INCLUDE_DIRS}
)

target_link_libraries(okon_caller
    PRIVATE
        okon
        ${benchmark_LIBRARIES}
        ${CMAKE_THREAD_LIBS_INIT}
)


add_custom_target(okon_btree_benchmark
    COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/okon_btree_benchmark.py
            $<TARGET_FILE:okon_caller> # Path to okon_caller
            10000 # Number of hashes to benchmark
            ${OKON_BENCHMARK_ORIGINAL_DB}
            555278656 # Number of hashes in original file
            ${OKON_BENCHMARK_BTREE_FILE}
    COMMENT  "Benchmarking btree on ${OKON_BENCHMARK_ORIGINAL_DB}"
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)
