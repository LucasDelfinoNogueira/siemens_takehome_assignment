"""
Solution 2b: Using pandas to find the two users
with the smallest login-time difference, with hardcoded JSON path.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

import pandas as pd
import os
from pandas import DataFrame, Series
from typing import Tuple


def load_records() -> DataFrame:
    """
    Load user records from the records.json file into a pandas DataFrame.

    Returns:
        DataFrame: DataFrame containing user records.
    """
    here = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(here, '..', '..', 'records.json'))
    
    return pd.read_json(path)

def find_closest_pair(df):
    """
    Find two users with the smallest difference in `last_login` time.

    Args:
        df (DataFrame): DataFrame with at least 'id' and 'last_login' columns.

    Returns:
        Tuple[Series, Series]: Two Series objects representing the closest user records.
    """
    df['last_login'] = pd.to_datetime(df['last_login'], utc=True)
    df = df.sort_values('last_login').reset_index(drop=True)
    df['diff'] = df['last_login'].diff().abs()
    idx = df['diff'].idxmin()
    
    return df.iloc[idx - 1], df.iloc[idx]


def main() -> None:
    """
    Load records and print the two user IDs and their login times
    with the smallest login-time difference.
    """
    df = load_records()
    row1, row2 = find_closest_pair(df)
    print(f"{row1['id']} {row1['last_login'].isoformat()}")
    print(f"{row2['id']} {row2['last_login'].isoformat()}")

if __name__ == '__main__':
    main()
