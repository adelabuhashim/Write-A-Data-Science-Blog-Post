def object_dtype(df):
    """
    printing the real data type of the object

    """
    
    if list(df.select_dtypes(include=['object']).columns) != [] :
    
        for column in df.select_dtypes(include=['object']).columns:

            print(column,type(df[column][0]))
    else:
        print('No complex data types :)')