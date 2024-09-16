# Benchmark

| encode                                      | json | jsonc | unit (μs) |
|:--------------------------------------------|-----:|------:|----------:|
| List of 65,536 booleans                     | 1.12 |  1.00 |   1302.82 |
| List of 16,384 ASCII strings                | 1.00 |  1.07 |   2860.55 |
| List of 4,096 floats                        | 1.00 |  1.01 |   2988.52 |
| List of 4,096 dicts with 1 int              | 1.00 |  1.03 |   1388.82 |
| Medium complex object                       | 1.00 |  1.01 |    138.68 |
| List of 4,096 strings                       | 1.07 |  1.00 |   5924.66 |
| Complex object                              | 1.02 |  1.00 |   1520.55 |
| Dict with 256 lists of 256 dicts with 1 int | 1.00 |  1.02 |  22991.89 |

| decode                                      | json | jsonc | unit (μs) |
|:--------------------------------------------|-----:|------:|----------:|
| List of 65,536 booleans                     | 1.00 |  1.31 |   1134.66 |
| List of 16,384 ASCII strings                | 1.02 |  1.00 |   1645.79 |
| List of 4,096 floats                        | 1.00 |  1.04 |   1088.77 |
| List of 4,096 dicts with 1 int              | 1.00 |  1.06 |   1286.10 |
| Medium complex object                       | 1.00 |  1.12 |     99.52 |
| List of 4,096 strings                       | 1.68 |  1.00 |    962.30 |
| Complex object                              | 1.14 |  1.00 |   1086.72 |
| Dict with 256 lists of 256 dicts with 1 int | 1.00 |  1.07 |  29428.03 |
