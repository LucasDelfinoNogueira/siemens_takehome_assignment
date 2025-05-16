#!/usr/bin/env python3
"""
Solution 2a: Using json and datetime to find the two users
with the smallest login-time difference, with hardcoded JSON path.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

import json
import os
from datetime import datetime
from typing import List, Dict, Tuple


def load_records() -> List[Dict[str, str]]:
    """
    Load records from the hard-coded records.json file located two levels up.

    Returns:
        List[Dict[str, str]]: List of user record dictionaries.
    """
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))

    with open(path) as f:
        return json.load(f)

def find_closest_pair(records):
    """
    Find two users with the smallest difference in `last_login` time.

    Args:
        records (List[Dict[str, str]]): List of user records with 'id' and 'last_login' keys.

    Returns:
        Tuple[str, datetime, str, datetime]: Tuple containing:
            - first user id
            - first login datetime
            - second user id
            - second login datetime
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


def main() -> None:
    """
    Load records and print the two user IDs and their login times
    with the smallest login-time difference.
    """
    records = load_records()
    id1, t1, id2, t2 = find_closest_pair(records)
    print(f"{id1} {t1.isoformat()}")
    print(f"{id2} {t2.isoformat()}")

if __name__ == '__main__':
    main()
