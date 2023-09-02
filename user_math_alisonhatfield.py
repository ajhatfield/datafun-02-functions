"""
Author: Alison Hatfield
Date: 9/1/2023

Purpose: Calculate the area of different sports fields/courts.
Compare the sports fields/courts to see the difference, sum, and max areas. 
Illustrate the math module and how to write defensive functions by trying them.

"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_area_of_sports_field(length, width): 

    #Return the area of a rectangle given the length and width

    logger.info(f"CALLING get_area_of_sports_field_area({length, width})")
    
    try: 
        area = length * width
        logger.info(f"The area of the sports field is {area}")
        return area 
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

#Calling get_area_of_sports_field with several different length and widths
football_field = get_area_of_sports_field(360,160)  #Area of Football Field
soccer_field = get_area_of_sports_field(360,225)  #Area of Soccer Field
lacrosse_field = get_area_of_sports_field(180, 330)  #Area of Lacrosse Field
tennis_court = get_area_of_sports_field(78,27)     #Area of Tennis Court

#Adding 3 more useful funtions that utilize math module
logger.info(f"abs difference of soccer and football fields = {math.fabs(football_field - soccer_field)}")
all_areas = [football_field, soccer_field, lacrosse_field, tennis_court]
logger.info(f"sum of all areas computed = {math.fsum(all_areas)}")
logger.info(f"largest field = {max(all_areas)}")


#At the end of the file add code from defensive math
logger.info("Explore some funtions in the Math module")
logger.info(f"math.comb(360,160) = {math.comb(360,160)}")
logger.info(f"math.ceil(360.3 * 4.7) = {math.ceil(360.3 * 4.7)}")
logger.info(f"math.floor(360.3 * 4.7) = {math.floor(360.3 * 4.7)}")
