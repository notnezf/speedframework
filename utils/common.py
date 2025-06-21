# utils/common.py

import os

def load_list_or_value(value):
    if os.path.exists(value):
        with open(value) as f:
            return f.read().splitlines()
    else:
        return [value]
