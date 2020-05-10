import pathlib

import pandas as pd

from hw4_q3 import *


fname = pathlib.Path('311_service_requests.zip')


def test_common_complaint():
    ans = common_complaint(fname)
    assert ans == ('HEATING', 73371)


def test_parking_borough():
    ans = parking_borough(fname)
    assert ans == 'BROOKLYN'
