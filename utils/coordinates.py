"""Helpers for parsing spatial coordinates."""

import numpy as np
import pandas as pd


def coord_split(value):
    """Convert comma-separated coordinates to a tuple, or return None if missing."""
    if pd.notna(value):
        return tuple(
            np.float64(coord) for coord in filter(pd.notna, value.split(","))
        )
    return None
