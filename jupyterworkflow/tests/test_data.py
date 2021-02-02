from jupyterworkflow.data import get_fremont_data
import pandas as pd

def test_fremont_data():
    assert all(data.columns ==['Total', 'East', 'West']) #this is to make sure the columns are right
    tssert isinstance(data.index, pd.DatetimeIndex)
