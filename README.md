# Benchmark (Apr 20, 2025)

| encode                                      |  json | json (setuptools) | jsonyx | reference time |
|:--------------------------------------------|------:|------------------:|-------:|---------------:|
| List of 256 booleans                        | 1.05x |             1.00x |  0.94x |        7.91 μs |
| List of 256 ASCII strings                   | 1.02x |             1.00x |  0.89x |       49.98 μs |
| List of 256 dicts with 1 int                | 0.98x |             1.00x |  1.03x |       89.74 μs |
| Medium complex object                       | 1.00x |             1.00x |  1.02x |      138.74 μs |
| List of 256 floats                          | 1.00x |             1.00x |  1.01x |      204.06 μs |
| List of 256 strings                         | 1.12x |             1.00x |  1.00x |      306.76 μs |
| Complex object                              | 1.05x |             1.00x |  1.04x |     1542.36 μs |
| Dict with 256 lists of 256 dicts with 1 int | 0.97x |             1.00x |  1.05x |    22982.71 μs |

| decode                                      |  json | json (setuptools) | jsonyx | reference time |
|:--------------------------------------------|------:|------------------:|-------:|---------------:|
| List of 256 booleans                        | 0.80x |             1.00x |  0.88x |        8.49 μs |
| List of 256 ASCII strings                   | 1.16x |             1.00x |  0.86x |       24.76 μs |
| List of 256 strings                         | 1.82x |             1.00x |  0.98x |       64.81 μs |
| List of 256 floats                          | 0.91x |             1.00x |  1.02x |       73.93 μs |
| List of 256 dicts with 1 int                | 0.89x |             1.00x |  0.90x |       89.81 μs |
| Medium complex object                       | 0.88x |             1.00x |  0.94x |      115.90 μs |
| Complex object                              | 1.10x |             1.00x |  1.00x |     1178.53 μs |
| Dict with 256 lists of 256 dicts with 1 int | 0.96x |             1.00x |  0.98x |    32229.35 μs |
