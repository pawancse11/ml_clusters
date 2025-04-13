import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import  StandardScaler
'''
lets load data first from the folder
define input and output path
'''
input_path =  'D:\ml_clusters\src\data\wine-clustering.csv'
output_path = 'D:\ml_clusters\src\data'

'''
define the funtion which will load data from given input path
'''
def load_data(path):
    data =  pd.read_csv(input_path)
    return data


'''
preprocess the data
'''
def preprocess_data(df):
    df.fillna(df.mean())
    features =  df.columns

    ##scale data
    sd_scale = StandardScaler()
    scaled_features =  sd_scale(df)

    scaled_features =  pd.DataFrame(scaled_features, columns=features)

    return scaled_features
    
'''
save scaled data in the output folder
'''
def save_processed_data(df, output_path):
    os.mkdir(os.path.dirname(output_path), exit_ok = True)
    df.to_save(output_path, index = False)
    


if __name__ == "__main__":
    #lead data set
    data = load_data(input_path)

    #preprocess data
    preprocess_df =  preprocess_data(data)

    #save data
    save_processed_data(preprocess_df,"../output_path/preprocess_df.csv" )


