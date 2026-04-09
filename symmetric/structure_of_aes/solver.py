#!/usr/bin/env python3

import numpy as np

matrix = np.array([
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
])


flag = matrix.tobytes('C')
print(flag.strip(b'"0x"'))


