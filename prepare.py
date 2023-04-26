import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('C:/Users/n.ushanov/Downloads/responce_train.csv')
df = df.drop(["client_id"], axis=1)

def text_to_int(data, columns):
    le = preprocessing.LabelEncoder()
    for col in columns:
        data[col] = le.fit_transform(data[col])
    return data

def clean(data):
    cols = list(data.keys())
    for col in cols:
        data[col].fillna(data[col].median(), inplace=True)
    return data


columns = ["education", "marital-status", "industry", "title", "tp-state", "tp-foreign", "job-type", "family-income", "registration-region", "fact-region", "postal-region", "last-loan-region", "region"]

df = text_to_int(df, columns)
df = clean(df)
