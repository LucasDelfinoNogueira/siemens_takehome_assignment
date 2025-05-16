#!/usr/bin/env python3
"""
Solution 2a: Using json and datetime to find the two users
with the smallest login-time difference, with hardcoded JSON path.
"""

import json
from datetime import datetime
import os

def load_records():
    """Load records from the hard-coded JSON file two levels up."""
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))
    
    with open(path) as f:
        return json.load(f)

def find_closest_pair(records):
    """
    Find two users with minimal login time difference.
    Returns a tuple: (id1, time1, id2, time2).
    """
    data = []
    for r in records:
        # parse ISO8601 with Z as UTC
        dt = datetime.fromisoformat(r['last_login'].replace('Z', '+00:00'))
        data.append((r['id'], dt))

    # sort by timestamp
    data.sort(key=lambda x: x[1])

    best = None
    min_diff = float('inf')
    for i in range(len(data) - 1):
        id1, t1 = data[i]
        id2, t2 = data[i + 1]
        diff = (t2 - t1).total_seconds()
        if diff < min_diff:
            min_diff = diff
            best = (id1, t1, id2, t2)

    return best

def main():
    """Main entry point."""
    records = load_records()
    id1, t1, id2, t2 = find_closest_pair(records)
    print(f"{id1} {t1.isoformat()}")
    print(f"{id2} {t2.isoformat()}")

if __name__ == '__main__':
    main()
