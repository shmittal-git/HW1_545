import numpy as np 
import pandas as pd


def extract_parameter(unit_name, parameter_name, index):
    try:
        #process = unit_operations_data[unit_name]
        #attribute = unit_operations_data[unit_name][parameter_name]
        value = unit_operations_data[unit_name][parameter_name][index]
        print(f'the output is {unit_name}_{parameter_name}_{value}')
    except(KeyError,IndexError):
        print('Invalid Input')
    
