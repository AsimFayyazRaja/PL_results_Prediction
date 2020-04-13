import pickle
import numpy as np
import pandas as pd
import sys

#home=sys.argv[1]
#away=sys.argv[2]

# open the saved model for random forest and label encoder for teams i.e. team name to integer conversion
with open("RandomForest.pkl", "rb") as input_file:
    clf = pickle.load(input_file)

with open("le_team.pkl", "rb") as input_file:
    le_team = pickle.load(input_file)
    
def list_all_teams():
    "returns list of all classes"
    return le_team.classes_

def get_probs(home,away):
    "returns probabilities of win, draw, loose when home and away teams are given as input"
    ht=le_team.transform([home])[0]
    at=le_team.transform([away])[0]
    df=pd.read_csv('preprocessed_data.csv')   # read clean CSV

    vector=df.loc[(df['HomeTeam']==ht) & (df['AwayTeam']==at)]  # get all results for those teams
    vector=vector.drop('FTR',axis=1)

    mean_cols=['HS','AS','HST','AST','HC','AC','HTR','WHH','WHD','WHA']
    v1=[]
    v1.append(ht)
    v1.append(at)
    for col in mean_cols:
        v1.append(np.mean(vector[col].values)+np.std(vector[col].values))   # make feature vector
    v1.append(v1[2]-v1[3])
    v1.append(v1[4]-v1[5])

    return clf.predict_proba(np.array(v1).reshape(1,-1))   # return prob from model's predictions