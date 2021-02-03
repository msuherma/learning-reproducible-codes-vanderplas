from jupyterworkflow.data import get_fremont_data
import pandas as pd
import numpy as np

def test_fremont_data():
    assert all(data.columns ==['Total', 'East', 'West']) #this is to make sure the columns are right
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time)==24) #to ensure 24 hour 
