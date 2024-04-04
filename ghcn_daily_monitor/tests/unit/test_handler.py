import json

import pytest

from ghcn_daily_monitor.ghcn_daily_monitor import app


def test_get_files():
    with open('samples/daily_all_sample.html', 'r') as file:
        file_contents = file.read()
    files = sorted(app.get_files(file_contents))
    test_files = sorted([
        ("ACW00011604.dly", "2024-03-20 13:06", "13", "K"),
        ("ACW00011647.dly", "2024-03-20 13:06", "114", "K"),
        ("AE000041196.dly", "2024-03-28 20:40", "629", "K")
    ])
    assert files == test_files

