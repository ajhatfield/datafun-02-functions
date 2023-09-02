'''
Author: Alison Hatfield
Date: 9/1/2023

Purpose: Make a copy of numeric_series.py and 
attempt to add another method and utilize it as an object in user_numeric_sports_alisonhatfield.py

'''

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

class NumericSeries:
    """
    A class (template) representing a numeric list of data with a name and units.

    Attributes:
        data (list): the data held by the object
        name (str): a descriptive name for the data
        units (str): the units associated with the data
    """

    def __init__(self, name, units, data):
        """
        Initialize the object when first created using the name, units, and data passed in through the constructor method.
        The two underscores before and after indicate this is a special method.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            data (list): the list of numeric data to be held by the object
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured

        """

        # initialize the object's attributes 
        # attribute is a special word for "data in an object"
        self.name = name
        self.units = units
        self.data = data

    # define methods that can be used on the object
    # method is a special word for "function in an object"
    # In Python, the first argument of a method is always self - the object itself
    def count(self):
        """ 
        Get the count of elements in the data list.

        @return: the count of elements
        """
        return len(self.data)

    def mean(self):
        """
        Calculate the mean of the data list
        @return: float - the mean of the data
        """
        return sum(self.data) / len(self.data)

    def median(self):
        """
        Calculate the median of the data.
        @return: float -  the median of the data
        """
        sorted_data = sorted(self.data)
        n = len(self.data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
        
    def sum(self):
        """ 
        Calculate the sum of the data.
        @return: the sum of the data
        """
        return sum(self.data)

    def variance(self):
        """
        Calculate the variance of the data.

        Returns:
            float: the variance of the data
        """
        n = len(self.data)
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / (n - 1)

    def standard_deviation(self):
        """
        Calculate the standard deviation of the data.

        Returns:
            float: the standard deviation of the data
        """
        return self.variance() ** 0.5
    
    def maximum(self):
        """
        Calculate the max of the data.

        Returns:
            float: the max of the data
        """
        return self.max(self.data)
    def minimum(self):
        """
        Calculate the min of the data.

        Returns:
            float: the min of the data
        """
        return self.min(self.data)

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericSeries with name={self.name}, units={self.units}, and {len(self.data)} data points: {self.data}"
        return str