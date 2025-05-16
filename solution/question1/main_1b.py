"""
Solution 1b: Print the 3 users closest to target as a pandas DataFrame.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

import pandas as pd
import os
from pandas import DataFrame


def load_records() -> DataFrame:
    """
    Load user records from the records.json file into a pandas DataFrame.

    Returns:
        DataFrame: DataFrame containing user records.
    """
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))
    
    return pd.read_json(path)


def main() -> None:
    """
    Load records, convert `last_login` to datetime, calculate time differences from
    the target timestamp, and print the 3 users with the smallest time difference.
    """
    df = load_records()
    df['last_login'] = pd.to_datetime(df['last_login'], utc=True)

    target = pd.Timestamp('2025-02-01T00:00:00Z')
    df['diff'] = (df['last_login'] - target).abs()

    result = df.nsmallest(3, 'diff').reset_index(drop=True)
    print(result)

if __name__ == '__main__':
    main()
