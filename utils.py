
from collections import defaultdict
import pandas as pd

def total_count(df, column_1, column_2, rename_column, possible_vals):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    column_1 - the column name you want to look through
    column_2 - the column you want to count values from
    rename_column - the column you want the original column_1 renamed to
    possible_vals - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    '''
    df = df[column_1].value_counts().reset_index()
    df.rename(columns={'index': rename_column, column_1: column_2}, inplace=True)
    new_df = defaultdict(int)
    #loop through list of possible values
    for val in possible_vals:
        #loop through rows
        for index in range(df.shape[0]):
            if val in df[rename_column][index]:
                new_df[val] += int(df[column_2][index])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [rename_column, column_2]
    new_df.sort_values('count', ascending=False, inplace=True)
    new_df.set_index(rename_column, inplace=True)
    return new_df


def separate_items(items_list):
    '''Separates the individual items from the list where different
       different items are together'''
    new_list = []
    for language in items_list:
        new_items = language.split(';')
        new_items = map(lambda x: x.strip(), new_items) # remove spaces from individual elements
        new_list.extend(list(new_items))

    return list(set(new_list))


def column_description(column_name, schema):
    '''Returns the description of the column from the schema'''
    return schema[schema['Column'] == column_name][schema.columns[-1]].values[0]


