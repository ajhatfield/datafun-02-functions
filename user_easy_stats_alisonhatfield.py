"""
Author: Alison Hatfield
Date: 9/1/2023

Purpose: Illustrate the built-in statistics module.
Analyze different stats functions for tempatures and ice cream sales

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

# Descriptive: Tempature Samples X
temp_data = [95, 32, 45, 51, 60, 67, 100, 97, 12, 10, 25, 98, 25, 5, 25, 82, 99, 87, 92, 101, 50]
# Descriptive: Ice Cream Sales Y
ice_cream_sales_data = [100, 25, 33, 50, 56, 150, 110, 15, 10, 30, 105, 20, 10, 10, 75, 115, 95, 125, 200, 45]

# Descriptive: Averages and measures of central tendency for temp data

mean_temp = statistics.mean(temp_data)
median_temp = statistics.median(temp_data)
mode_temp = statistics.mode(temp_data)

# Descriptive: Averages and measures of central tendency for ice cream sales data

mean_sales = statistics.mean(ice_cream_sales_data)
median_sales = statistics.median(ice_cream_sales_data)
mode_sales = statistics.mode(ice_cream_sales_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f" tempature mean   = {mean_temp:.2f}")
logger.info(f"tempature median = {median_temp:.2f}")
logger.info(f"tempature mode   = {mode_temp:.2f}")
logger.info(f"sales mean   = {mean_sales:.2f}")
logger.info(f"sales median = {median_sales:.2f}")
logger.info(f"sales mode   = {mode_sales:.2f}")

# Descriptive: Measures of spread for tempature data

var_temp = statistics.variance(temp_data)
stdev_temp = statistics.stdev(temp_data)
lowest_temp = min(temp_data)
highest_temp = max(temp_data)
range_temp = lowest_temp, highest_temp

# Descriptive: Measures of spread for ice cream sales

var_sales = statistics.variance(ice_cream_sales_data)
stdev_sales = statistics.stdev(ice_cream_sales_data)
lowest_sales = min(ice_cream_sales_data)
highest_sales = max(ice_cream_sales_data)
range_sales = lowest_sales, highest_sales

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)
logger.info(f"var of tempature data    = {var_temp:.2f}")
logger.info(f"stdev of tempature data   = {stdev_temp:.2f}")
logger.info(f"lowest of tempature data = {lowest_temp:.2f}")
logger.info(f"highest of tempature data = {highest_temp:.2f}")
logger.info(f"range of tempature data = {range_temp}")
logger.info(f"var of ice cream sales    = {var_sales:.2f}")
logger.info(f"stdev of ice cream sales  = {stdev_sales:.2f}")
logger.info(f"lowest of ice cream sales = {lowest_sales:.2f}")
logger.info(f"highest of ice cream sales = {highest_sales:.2f}")
logger.info(f"range of ice cream sales = {range_sales}")


