import json
from hamilton.function_modifiers import (
    parameterize_sources, 
    parameterize_values,
    parameterize,
    source,
    value
)
import pandas as pd
import numpy as np
import helper_functions
from helper_functions import wkpentopounds
import ast

# test_dict = {
#     'c21111': {'var1': source('e14111'), 'var2': source('e14112')}
#     }
    
# @parameterize_sources(**test_dict)
# def nansum(var1: pd.Series, var2 :pd.Series, var3:pd.Series = pd.Series) -> pd.Series:

#     return var1 + var2 + var3

def update_config(config:dict) -> dict:
    new_config = config
    for function, code_dict in config.items():
        new_code_dict = code_dict
        for code, variables_dict in code_dict.items():
            new_variables_dict = variables_dict
            for variable, input in variables_dict.items():
                if "source" in input:
                    temp_str = input.split('(')[1]
                    temp_str = temp_str.split(')')[0]
                    new_variables_dict[variable] = source(temp_str)
                elif "value" in input:
                    temp_str = input.split('(')[1]
                    temp_str = temp_str.split(')')[0]
                    new_variables_dict[variable] = value(temp_str)
            new_code_dict[code] = new_variables_dict
        new_config[function] = new_code_dict
    
    return new_config

config = json.load(open('config.json'))
config = update_config(config)
config = config["c_codes_shops"]

@parameterize(**config)
def c_codes_shops(shop: pd.Series, fincode: pd.Series, paid1: pd.Series, code_fincodes:str, shop_str:str) -> pd.Series:
    
    shop_func = getattr(helper_functions, shop_str)
    df = pd.DataFrame()
    
    df['in_shop'] = shop_func(shop)
    code_fincodes = ast.literal_eval(code_fincodes)
    df['in_fincodes'] = fincode.isin(code_fincodes)
    df['new_col'] = (df['in_fincodes']) & (df['in_shop'])
    df['wkpentopounds'] = paid1.apply(wkpentopounds)
    print(df)
    df.loc[~df['new_col'], 'wkpentopounds'] = 0

    return df['wkpentopounds']
