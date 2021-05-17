# Time series data preprocessing class
import pandas as pd


class TimeSeriesPreprocessing:
    # Class attribute
    # class attributes are used to define properties that should have the same value for every class instance.
    about = "This is a class for time series data preprocessing"

    # class initial state declaration
    def __init__(self, data_path):
        # create instance attributes and assign it to the value of the parameter
        self.data = pd.read_csv(data_path)

    def preprocess(self):
        # preprocessing steps
        return self.data



