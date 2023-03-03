from hamilton import driver
from hamilton import base
import hamilton_demo
import pandas as pd

input_df = pd.DataFrame({
                    "e14111": [1, 2, 3, 4, 5],
                    "e14112": [1, 1, 1, 1, 1],
                    "e14113": [1, 1, 2, 2, 3],
                    "shop": ['70', '140', '1130', '340', '680'],
                    "fincode": ['14111', '14112', '14112', '14115', '14118'],
                    'paid1': [1, 9, 5, 3, 2]
                    })


adapter = base.SimplePythonGraphAdapter(base.PandasDataFrameResult())
dr = driver.Driver(input_df, hamilton_demo, adapter=adapter)

output_cols = ['c21111l', 'c21111w']

result = dr.execute(output_cols)

print(result)
