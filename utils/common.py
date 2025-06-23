# utils/common.py

import os

def loadListOrValue(value):
    if os.path.exists(value):
        with open(value) as f:
            return f.read().splitlines()
    else:
        return [value]
