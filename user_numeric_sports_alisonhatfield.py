'''

Author: Alison Hatfield 
Date: 9/1/2023 

Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to different teams basketball games. 

Sports adds:

- a team attribute

'''

# From the name of the module (the file name without .py), import the class we want to inherit from
from user_numeric_alisonhatfield import NumericSeries

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


class NumericSportsSeries(NumericSeries):
    """
    A class representing a numeric series customized for sports data.

    (Additional) Attributes:
       team (string): the team where the data was collected
    """

    def __init__(self, name, units, data, team):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            team (str): the team the data was collected on

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.team = team

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericSportsSeries with name={self.name}, units={self.units}, location={self.team}, and {len(self.data)} data points: {self.data}"
        return str




if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "Mondays Game"
    units1 = "Points per Quarter"
    data1 = [25, 15, 10, 30]
    loc = "Nebraska Cornhuskers"

    object1 = NumericSportsSeries(name1, units1, data1, loc)

  
    name2 = "Thursday Game"
    units2 = "Points per Quarter"
    data2 = [12, 16, 21, 36]
    loc2 = "Indiana Hoosiers"

    object2 = NumericSportsSeries(name2, units2, data2, loc2)

    
    # Create another object 

    # use range() to create a list of values from 10 to 41
    # list() converts the range object to a list
    # range() is a generator - it creates a sequence of numbers without storing them in memory
    # The arguments in range are from (inclusive) and to (exclusive)
    data3 = list(range(10, 41))
    name3 = "Fridays Game"
    units3 = "Points per Player"
    loc3 = "Missouri Tigers"

    object3 = NumericSportsSeries(name3, units3, data3, loc3)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]


    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")

