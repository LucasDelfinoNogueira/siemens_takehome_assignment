"""
Solution 1a: print full JSON objects for the 3 users closest to target.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

import json
from datetime import datetime, timezone
import os
from typing import List, Dict, Any


def load_records() -> List[Dict[str, Any]]:
    """
    Load and return a list of user records from the records.json file.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a user record.
    """
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))

    with open(path) as f:
        return json.load(f)


def find_closest(records: List[Dict[str, Any]], target: datetime, n: int = 3) -> List[Dict[str, Any]]:
    """
    Find the n records whose 'last_login' timestamps are closest to the given target datetime.

    Args:
        records (List[Dict[str, Any]]): List of user records.
        target (datetime): Target datetime to compare against.
        n (int, optional): Number of closest records to return. Defaults to 3.

    Returns:
        List[Dict[str, Any]]: List of the n closest user records.
    """
    diffs = []
    for r in records:
        dt = datetime.fromisoformat(r['last_login'].replace('Z', '+00:00'))
        diff = abs((dt - target).total_seconds())
        diffs.append((diff, r))

    diffs.sort(key=lambda x: x[0])
    return [item[1] for item in diffs[:n]]


def main() -> None:
    """
    Main function that loads records, finds the closest logins to the target datetime,
    and prints their key-value pairs.
    """
    records = load_records()
    target = datetime(2025, 2, 1, 0, 0, tzinfo=timezone.utc)

    closest = find_closest(records, target)
    for rec in closest:
        for k, v in rec.items():
            print(f"{k}: {v}")
        print()


if __name__ == '__main__':
    main()
