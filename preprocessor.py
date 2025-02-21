import pandas as pd

def preprocess(df,regn_df):

    df = df[df['Season'] == 'Summer']
    df.drop_duplicates(inplace=True)
    df = df.merge(regn_df, on='NOC', how='left')
    df = pd.concat([df, pd.get_dummies(df['Medal']).astype(int)], axis=1)
    return df