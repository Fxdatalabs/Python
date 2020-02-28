'''
Problem 2
Use the python library pandas to import some klines from any open API you can find and save them into a pandas dataframe.
Print out the first 5 rows and the last 5 rows of the dataframe. Do not send us your private API key.
'''

import pandas as pd

def print_data(path):
    data_frame = pd.read_csv(path)
    print(data_frame.head() , data_frame.tail(), sep='\n')


if __name__ == '__main__':
    path = 'https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv'
    print_data(path)



