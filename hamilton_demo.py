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

test_dict = {
    'c21111': {'var1': source('e14111'), 'var2': source('e14112')}
    }
    


@parameterize_sources(**test_dict)
def nansum(var1: pd.Series, var2 :pd.Series, var3:pd.Series = pd.Series) -> pd.Series:

    
    
    return var1 + var2 + var3










# shops_dict = {
#     'c21111l': {
#         'shop': source('shop'), 'fincode':source('fincode'), 'paid1':source('paid1')
#         },
# }

# @parameterize_sources(**shops_dict)
# def c_codes_shops(shop: pd.Series, fincode: pd.Series, paid1: pd.Series) -> pd.Series:
#     return paid1