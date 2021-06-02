import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pdb


def get_data():
    """ Load Dataset,drops columns and filters by survey completed"""
    
    # data = pd.read_csv ('D:\dev\\rocky\\static\\survey_numeric.csv')
    data = pd.read_csv('/Users/d18127085/Documents/survey/data/survey_numeric.csv')
    data.drop (columns = [ 'startDate', 'endDate', 'status', 'ipAddress', 'progress',
                            'duration', 'recordedDate', 'recipientLastName', 'recipientFirstName',
                            'recipientEmail','externalDataReference', 'locationLatitude', 'locationLongitude',
                            'distributionChannel', 'userLanguage','_recordId','QID143','QID17','QID121_13_TEXT'],
                inplace = True)
    # Deletes first row
    data = data.iloc[1:]
    # Filter by completed surveys
    data = data[data['finished'] == '1']
    return data 


def transform(score):
    "Transforms the scores in a high/low scale"
    if (score) <= 5:
        return "Low"
    else:
        return "High"


def binary_data(data, tech):
    " Divides data and binarize values on target"
    
    X = data.loc[:,'QID120':'QID45_5']
    y = data[tech].astype(int) 
    y = y.apply(lambda score: transform(score)) 
    map_binary = {'High':(1), 'Low':(0)}
    y = y.map(map_binary)
    #scaler = StandardScaler()
    #scaler.fit(X)
    #X = scaler.transform(X)
    return X, y, 
 

def train_test(X, y):
    "Split data train and test"
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    return X_train, X_test, y_train, y_test


"""
 def continuous():
     data = get_data()
     X = data.loc[:,'QID120':'QID45_5']
     y = data['SC01'].astype(int)
     return X,y
     print ('y size:', y.shape)
     print("---------")
     print ('X size:', X.shape)
"""  
 


def main():
    data = get_data()
    X,y= binary_data(data)
    X_train, X_test, y_train, y_test = train_test( y, X)


 
   




    

