import pandas as pd

def object_dtype(df):
    """
    printing the real data type of the object

    """
    
    if list(df.select_dtypes(include=['object']).columns) != [] :
    
        for column in df.select_dtypes(include=['object']).columns:

            print(column,type(df[column][0]))
    else:
        print('No complex data types :)')
        

def fix_price(df, column='price'):
    """
    fix price format from %d,%d$ --> %f

    args: 
         - dataframe contains the columns
         - column name
    """
    df[column] = df[column].str.replace(',', '').str.replace('$', '').astype(float)
    
    
def fix_date(df, column='date', format='%Y-%m-%d'):
    """
    fix date

    args: 
         - dataframe 
         - column name
         - format
    """
    
    df[column] = pd.to_datetime(df[column], format='%Y-%m-%d')
    
    
def df_shape(df):
    """
    printing the shape of the dataframe
    """
    print('the df has {} rows and {} columns'.format(df.shape[0],df.shape[1]))