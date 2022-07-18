import pandas as pd


def dataframe_creator(col1, col2, val1, val2):
    """
    Creates a dataframe from the data.
    """
    dataframe = pd.DataFrame({col1: val1, col2: val2})
    return dataframe

def dataframe_writer(dataframe, filename):
    """
    Writes the dataframe to a csv file.
    """
    dataframe.to_csv(filename)