import json

import pandas as pd
import pytest

from ghcn_daily_monitor.function import app


def test_get_files():
    with open('samples/daily_all_sample.html', 'r') as file:
        file_contents = file.read()
    df1 = app.get_files(file_contents, '2024-03-28').reset_index(drop=True)
    df2 = pd.DataFrame([
        ("AE000041196.dly", "2024-03-28 20:40", "629", "K")
    ], columns=['file_name', 'last_modified', 'size_value', 'size_unit'])
    df2['last_modified'] = pd.to_datetime(df2['last_modified'], format='%Y-%m-%d %H:%M')

    assert hash(df1.to_json()) == hash(df2.to_json())

