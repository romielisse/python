#!/usr/bin/env python3

"""
This module provides functions for converting feet to meters. 
"""
 
def to_meters(feet):
    meters = feet * 0.3048
    return meters

def to_feet(meters):
    feet = meters / 0.3048
    return feet
