from hamilton.function_modifiers import parameterize_values

CONFIG = {
     #output name        # doc string               # input value to function
    ('SOME_OUTPUT_NAME', 'Doc string for this thing'): 'value to pass to function',
    ("<code>"          , ''                         ): '<dependant variable>',
    ("a002"            , ''                         ): 'rfrom',
    ("a048"            , ''                         ): 'dv02',
}

# parameter matches the name of the argument in the function below
@parameterize_values(parameter='dependant_variable', assigned_output=CONFIG)
def multiply_code_value(dependant_variable):
    """Multiplies the value by 2

    Parameters
    ----------
    dependant_variable : int
        code value to multiply

    Returns
    -------
    int
        dependant variable multiplied by 2
    """    
    
    dependant_variable = dependant_variable * 2
    
    return dependant_variable


# Using the example in the config above. 

a002 = rfrom * 2
a048 = dv02 * 2
