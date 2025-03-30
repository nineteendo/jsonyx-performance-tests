# Benchmark (Mar 29, 2025)

| encode                                      |  json | jsonc | jsonyx | reference time |
|:--------------------------------------------|------:|------:|-------:|---------------:|
| List of 256 booleans                        | 1.05x | 1.00x |  0.97x |        6.69 μs |
| List of 256 ASCII strings                   | 0.81x | 1.00x |  0.96x |       47.44 μs |
| List of 256 dicts with 1 int                | 0.94x | 1.00x |  1.11x |       82.78 μs |
| Medium complex object                       | 0.95x | 1.00x |  1.09x |      118.56 μs |
| List of 256 floats                          | 1.02x | 1.00x |  1.02x |      157.28 μs |
| List of 256 strings                         | 1.44x | 1.00x |  1.11x |      295.94 μs |
| Complex object                              | 1.04x | 1.00x |  1.06x |     1514.53 μs |
| Dict with 256 lists of 256 dicts with 1 int | 0.95x | 1.00x |  1.13x |    22693.31 μs |

| decode                                      |  json | jsonc | jsonyx | reference time |
|:--------------------------------------------|------:|------:|-------:|---------------:|
| List of 256 booleans                        | 0.87x | 1.00x |  1.34x |        6.77 μs |
| List of 256 ASCII strings                   | 0.78x | 1.00x |  1.42x |       28.49 μs |
| List of 256 dicts with 1 int                | 0.94x | 1.00x |  1.30x |       76.36 μs |
| List of 256 floats                          | 0.97x | 1.00x |  1.07x |       76.51 μs |
| List of 256 strings                         | 0.91x | 1.00x |  1.56x |       84.64 μs |
| Medium complex object                       | 0.92x | 1.00x |  1.44x |      102.71 μs |
| Complex object                              | 1.06x | 1.00x |  1.06x |     1163.69 μs |
| Dict with 256 lists of 256 dicts with 1 int | 0.98x | 1.00x |  1.13x |    37174.33 μs |
