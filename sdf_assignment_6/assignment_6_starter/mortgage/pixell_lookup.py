"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: {kamaldeep kaur }
Date: {11-11-2023}
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = [5, 10, 15, 20, 25, 30] 

class MortgageRate (Enum):
    """
    An enumeration to store the mortgage rate options 
    """
FIXED_5: 0.0500
FIXED_3: 0.0579
FIXED_1: 0.0589
VARIABLE_5: 0.0650
VARIABLE_3: 0.0660
VARIABLE_1: 0.0679
class MortgageFrequency(Enum):
    """
    An enumeration to store the payment frequency options 
    """
MONTHLY: 12
BI_WEEKLY: 26
WEEKLY: 52

















