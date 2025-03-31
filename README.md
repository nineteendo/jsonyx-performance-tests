# Benchmark (Mar 31, 2025)

| encode                                      |  json | json (setuptools) | jsonyx | reference time |
|:--------------------------------------------|------:|------------------:|-------:|---------------:|
| List of 256 booleans                        | 1.05x |             1.00x |  1.01x |        6.64 μs |
| List of 256 ASCII strings                   | 0.81x |             1.00x |  0.94x |       48.55 μs |
| List of 256 dicts with 1 int                | 0.94x |             1.00x |  1.11x |       83.11 μs |
| Medium complex object                       | 0.95x |             1.00x |  1.11x |      118.07 μs |
| List of 256 floats                          | 0.98x |             1.00x |  1.00x |      162.88 μs |
| List of 256 strings                         | 1.38x |             1.00x |  1.08x |      305.67 μs |
| Complex object                              | 1.04x |             1.00x |  1.06x |     1520.85 μs |
| Dict with 256 lists of 256 dicts with 1 int | 0.95x |             1.00x |  1.43x |    22730.57 μs |

| decode                                      |  json | json (setuptools) | jsonyx | reference time |
|:--------------------------------------------|------:|------------------:|-------:|---------------:|
| List of 256 booleans                        | 0.88x |             1.00x |  1.35x |        6.85 μs |
| List of 256 ASCII strings                   | 0.86x |             1.00x |  1.36x |       28.77 μs |
| List of 256 dicts with 1 int                | 0.94x |             1.00x |  1.34x |       75.73 μs |
| List of 256 floats                          | 1.02x |             1.00x |  1.07x |       76.89 μs |
| List of 256 strings                         | 0.88x |             1.00x |  1.52x |       87.74 μs |
| Medium complex object                       | 0.89x |             1.00x |  1.40x |      107.20 μs |
| Complex object                              | 1.05x |             1.00x |  1.08x |     1165.61 μs |
| Dict with 256 lists of 256 dicts with 1 int | 0.96x |             1.00x |  1.20x |    35449.94 μs |
