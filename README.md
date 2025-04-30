# Benchmark (Apr 30, 2025)

| encode                                      |  json | json (setuptools) | jsonyx | reference time |
|:--------------------------------------------|------:|------------------:|-------:|---------------:|
| List of 256 booleans                        | 1.05x |             1.00x |  0.95x |        7.88 μs |
| List of 256 ASCII strings                   | 1.06x |             1.00x |  0.44x |       50.41 μs |
| List of 256 floats                          | 0.99x |             1.00x |  1.02x |      202.59 μs |
| List of 256 dicts with 1 int                | 1.00x |             1.00x |  0.85x |       90.00 μs |
| Medium complex object                       | 1.05x |             1.00x |  0.86x |      138.75 μs |
| List of 256 strings                         | 1.19x |             1.00x |  0.96x |      305.92 μs |
| Complex object                              | 1.12x |             1.00x |  1.03x |     1525.09 μs |
| Dict with 256 lists of 256 dicts with 1 int | 1.00x |             1.00x |  0.86x |    22905.82 μs |

| decode                                      |  json | json (setuptools) | jsonyx | reference time |
|:--------------------------------------------|------:|------------------:|-------:|---------------:|
| List of 256 booleans                        | 0.83x |             1.00x |  0.93x |        8.18 μs |
| List of 256 ASCII strings                   | 1.14x |             1.00x |  0.83x |       24.89 μs |
| List of 256 floats                          | 0.93x |             1.00x |  0.96x |       71.39 μs |
| List of 256 dicts with 1 int                | 0.91x |             1.00x |  1.00x |       85.92 μs |
| Medium complex object                       | 0.92x |             1.00x |  1.02x |      111.12 μs |
| List of 256 strings                         | 1.81x |             1.00x |  0.99x |       63.94 μs |
| Complex object                              | 1.17x |             1.00x |  1.03x |     1085.54 μs |
| Dict with 256 lists of 256 dicts with 1 int | 0.94x |             1.00x |  0.99x |    32558.82 μs |
