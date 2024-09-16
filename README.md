# Benchmark

| encode                                      | json | jsonc | unit (μs) |
|:--------------------------------------------|-----:|------:|----------:|
| List of 65,536 booleans                     | 1.00 |  0.93 |   1568.74 |
| List of 16,384 ASCII strings                | 1.00 |  1.12 |   2830.72 |
| List of 4,096 floats                        | 1.00 |  1.00 |   2996.67 |
| List of 4,096 dicts with 1 int              | 1.00 |  1.05 |   1369.86 |
| Medium complex object                       | 1.00 |  0.99 |    140.46 |
| List of 4,096 strings                       | 1.00 |  0.93 |   5979.93 |
| Complex object                              | 1.00 |  0.98 |   1590.89 |
| Dict with 256 lists of 256 dicts with 1 int | 1.00 |  1.05 |  22387.50 |

| decode                                      | json | jsonc | unit (μs) |
|:--------------------------------------------|-----:|------:|----------:|
| List of 65,536 booleans                     | 1.00 |  1.30 |   1177.90 |
| List of 16,384 ASCII strings                | 1.00 |  0.89 |   1679.06 |
| List of 4,096 floats                        | 1.00 |  1.04 |   1086.71 |
| List of 4,096 dicts with 1 int              | 1.00 |  1.08 |   1270.86 |
| Medium complex object                       | 1.00 |  1.13 |    100.01 |
| List of 4,096 strings                       | 1.00 |  0.60 |   1615.06 |
| Complex object                              | 1.00 |  0.87 |   1237.70 |
| Dict with 256 lists of 256 dicts with 1 int | 1.00 |  1.06 |  29709.79 |
