import json
from hamilton.function_modifiers import parameterize
import pandas as pd
import numpy as np
import helper_functions
from helper_functions import wkpentopounds, update_config
import ast
from functools import reduce
from operator import add

config = json.load(open('config.json'))
config = update_config(config)

parameterize(sum_sources, **nansum2_config)

def sum_sources(**kwargs):
    return reduce(kwargs.values(), add)


nansum2_config = config["nansum2"]
@parameterize(**nansum2_config)
def nansum2(var1: pd.Series, var2:pd.Series) -> pd.Series:
    return var1 + var2


nansum3_config = config["nansum3"]
@parameterize(**nansum3_config)
def nansum3(var1: pd.Series, var2:pd.Series, var3:pd.Series) -> pd.Series:
    return var1 + var2 + var3
        

shops_config = config["c_codes_shops"]

@parameterize(**shops_config)
def c_codes_shops(shop: pd.Series, fincode: pd.Series, paid1: pd.Series, code_fincodes:str, shop_str:str) -> pd.Series:
    
    shop_func = getattr(helper_functions, shop_str)
    df = pd.DataFrame()
    
    df['in_shop'] = shop_func(shop)
    code_fincodes = ast.literal_eval(code_fincodes)
    df['in_fincodes'] = fincode.isin(code_fincodes)
    df['new_col'] = (df['in_fincodes']) & (df['in_shop'])
    df['wkpentopounds'] = paid1.apply(wkpentopounds)
    df.loc[~df['new_col'], 'wkpentopounds'] = 0

    return df['wkpentopounds']
