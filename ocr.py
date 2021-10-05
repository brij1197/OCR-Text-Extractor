import pandas
from functools import lru_cache

@lru_cache(maxsize=None) #Caching of objects
class OCR:
    def __init__(self, filename: str):
        """
            Initialises and object of a class with a dataframe that is read from the csv provided with the object.
        """
        self.df = pandas.read_csv("./csvs/"+filename+".csv", index_col=False)

    def filterSpannedText(self, x0: int, y0: int, x2: int, y2: int):
        """
            Function that returns a set of spanned text
        """
        # Returns values if x2 values present in the dataframe are greater than the x0 value provided by the user and if x0 values present in the dataframe are lesser than the x2 value provided by the user.
        filterX = ((self.df["x2"] > x0) & (self.df["x0"] < x2))
        # Returns values if y2 values present in the dataframe are greater than the y0 value provided by the user and if y0 values present in the dataframe are lesser than the y2 value provided by the user.
        filterY = ((self.df["y2"] > y0) & (self.df["y0"] < y2))
        return(filterX & filterY)

    def spanWords(self, x0: int, y0: int, x2: int, y2: int):
        """
            Function that returns a set of texts that are spanned using the filter
        """
        df_filter = self.filterSpannedText(x0=x0, y0=y0, x2=x2, y2=y2)
        sorted_data = self.df[df_filter].sort_values(by=["y0", "x0"])
        all_texts = sorted_data["Text"].tolist()
        return " ".join(all_texts)