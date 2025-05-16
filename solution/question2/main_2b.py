"""
Solution 2b: Using pandas to find the two users
with the smallest login-time difference, with hardcoded JSON path.
"""

import pandas as pd
import os

def load_records():
    """Load records from the hard‑coded JSON file two levels up."""
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))
    
    return pd.read_json(path)

def find_closest_pair(df):
    """
    Find two users with minimal login time difference.
    Returns two pandas Series: row1, row2.
    """
    df['last_login'] = pd.to_datetime(df['last_login'], utc=True)
    df = df.sort_values('last_login').reset_index(drop=True)
    df['diff'] = df['last_login'].diff().abs()
    idx = df['diff'].idxmin()
    
    return df.iloc[idx - 1], df.iloc[idx]

def main():
    """Main entry point."""
    df = load_records()
    row1, row2 = find_closest_pair(df)
    print(f"{row1['id']} {row1['last_login'].isoformat()}")
    print(f"{row2['id']} {row2['last_login'].isoformat()}")

if __name__ == '__main__':
    main()
