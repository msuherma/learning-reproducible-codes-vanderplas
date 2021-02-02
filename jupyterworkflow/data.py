from urllib.request import urlretrieve
import pandas as pd
import os

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename = "fremont.csv", url=FREMONT_URL, force_download=False):
    '''
    This function is used to prepare the data:
    a) download the data from assigned URL (FREMONT DATA)
    b) parse the date of the data using pandas
    c) rename the column to simplify it, using columns name: ['Total', 'East', 'West']
    ------------
    Parameters:
    ------------
    filename: string (optional)
        location to save the data
    url: string (optional)
        web location of the data
    force_download: bool (optional)
        if True, force redownload of data
    ------------
    Returns
    ------------
    data : pandas.DataFrame
        The fremont bridge data contains passing bike data.
    '''
    if force_download or not os.path.exists(filename):
        urlretrieve(url, 'freemont.csv')
    data = pd.read_csv('fremont.csv', index_col = 'Date', parse_dates=True)
    data.columns = ['Total', 'East', 'West']
    return data