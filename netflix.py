import pandas as pd
import os
import numpy as np
import requests
import matplotlib as plt
import seaborn as sns



def directory(s):
    files = os.listdir(s)
    return files, os.getcwd()


def open_csv(s):
    files = os.listdir(s)
    for file in files:
        if ".csv" in file:    
            curr_dir = os.path.join(s,file)
            data = pd.read_csv(curr_dir,encoding='latin')
            
        else:
            print( s + " Does not contain any csv file format")
    return data
            
                       

  

def path_exist(s):
    if os.path.exists(s):
        print(s + " exists")
    else:
        print(s + " Does not exist")





store_df = open_csv('C:/Users/pc/Downloads/Store')
netflix_df = open_csv('.')

bank_df = open_csv('C:/Users/pc/Downloads/Bank_information')



def data_info(df):
    shape = df.shape
    print("The shape: {}".format(shape))
    check_null = df.isnull().sum()
    print("The total null data is :".format(check_null))
   

netflix_infos = data_info(netflix_df)




   
    
    







