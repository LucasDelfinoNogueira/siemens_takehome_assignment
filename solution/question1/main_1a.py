"""
Solution 1a: print full JSON objects for the 3 users closest to target.
"""

import json
from datetime import datetime, timezone
import os

def load_records():
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))
    
    with open(path) as f:
        return json.load(f)

def find_closest(records, target, n=3):
    """
    Return the n record dicts whose last_login is
    closest to target (either before or after).
    """
    diffs = []
    for r in records:
        dt = datetime.fromisoformat(r['last_login'].replace('Z', '+00:00'))
        diff = abs((dt - target).total_seconds())
        diffs.append((diff, r))

    # sort by diff, pick top n
    diffs.sort(key=lambda x: x[0])
    
    return [item[1] for item in diffs[:n]]

def main():
    records = load_records()
    target = datetime(2025, 2, 1, 0, 0, tzinfo=timezone.utc)

    closest = find_closest(records, target)
    for rec in closest:
        # print each key/value pair
        for k, v in rec.items():
            print(f"{k}: {v}")
        print()  # blank line between records

if __name__ == '__main__':
    main()
