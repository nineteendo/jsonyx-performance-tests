#!/usr/bin/env python
import json

import jsonc

decoder = jsonc.JSONDecoder()
s = json.dumps([True] * 65_536)
for _ in range(1_000):
    decoder.decode(s)
