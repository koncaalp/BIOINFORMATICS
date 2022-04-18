import pandas as pd
import numpy as np
from numpy import where

distance_dict = {'Human':(0,1,3,7), 'Chimp':(1,0,2,6), 'Pig':(3,2,0,4), 'Cat':(7,6,4,0)}

phylogeny = {}

df = pd.DataFrame(distance_dict,index=list(distance_dict.keys()))
# print(df)

def calc_most_related(df): # find the most related pair
    most_related = {}
    for species in df.index:
        smallest_distance = df[species].nsmallest(2).sum()
        most_related[species] = smallest_distance
    # print(most_related)
    return most_related


def calc_selected_min(most_related): # find the smallest distance among the most related pairs
    selected_min = min(most_related.values())
    # print(selected_min)
    return selected_min



# most_related = calc_most_related(df)
# selected_min = calc_selected_min(most_related)

def get_min_indices(df,selected_min): # find the indices of the smallest distance
    min_index = df.iloc[where(df.values == selected_min)].index
    min_pair = str(tuple(min_index))
    # print(min_pair)
    # print(min_index)
    return min_index,min_pair

# min_index, min_pair = get_min_indices(df,selected_min)

def update_phylogeny(min_pair, selected_min): # update the phylogeny dictionary
    phylogeny[min_pair] = selected_min / 2
    # print(phylogeny)
    return phylogeny

# update_phylogeny(min_pair, selected_min)

def cal_upgma_cluster(df, min_index): # calculate the upgma cluster for the given min_index
    merged_results = df.loc[min_index,:].sum() / 2
    merged_results.drop(min_index,inplace = True)
    return merged_results

# merged_results = cal_upgma_cluster(df, min_index)

def restruct_upgma(df,min_index,min_pair): #Merge the two cluster names in the df
    df.rename(columns = {min_index[0]:min_pair},
    index = {min_index[0]:min_pair}, inplace = True)
    df.drop(min_index[1], axis = 0, inplace = True)
    df.drop(min_index[1], axis = 1, inplace = True)

def upgma_merge_cluster(df,min_pair,merged_results): # Calculate the new distance matrix
    df.loc[df[min_pair] > 0,min_pair] = merged_results
    df.loc[min_pair,df[min_pair] > 0] = merged_results
    return df


# restruct_upgma(df,min_index,min_pair)
# upgma_merge_cluster(df,min_pair,merged_results)
# print(df)

def run_upgma(df):
    while df.shape != (1,1):
        most_related = calc_most_related(df)
        selected_min = calc_selected_min(most_related)
        min_index, min_pair = get_min_indices(df,selected_min)
        phylogeny = update_phylogeny(min_pair, selected_min)
        merged_results = cal_upgma_cluster(df, min_index)
        restruct_upgma(df,min_index,min_pair)
        upgma_merge_cluster(df,min_pair,merged_results)
    return phylogeny

print(run_upgma(df))