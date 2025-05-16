"""
Solution 1b: Print the 3 users closest to target as a pandas DataFrame.
"""

import pandas as pd
import os

def load_records():
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))
    
    return pd.read_json(path)

def main():
    df = load_records()
    # Transforms las_login to datetime
    df['last_login'] = pd.to_datetime(df['last_login'], utc=True)

    target = pd.Timestamp('2025-02-01T00:00:00Z')
    df['diff'] = (df['last_login'] - target).abs()

    result = (
        df
        .nsmallest(3, 'diff')
        .reset_index(drop=True)
    )

    # Print result
    print(result)

if __name__ == '__main__':
    main()
