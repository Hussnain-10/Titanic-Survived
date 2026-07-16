import pandas as pd
def clean_data(path):
    df=pd.read_csv(path)
    df['Title']=df['Name'].str.extract(r'(Mr.|Mrs.|Miss.|Dr.)')
    df['Title'].isnull().sum()
    df['Title']=df['Title'].fillna('Other')
    df['Title'].isnull().sum()
    df['Age']=df['Age'].fillna(df['Age'].median())
    df['TicketGroupSize']=df.groupby('Ticket')['Ticket'].transform('count')
    df['TicketGroupSize'].value_counts()
    df['TicketGroupSize']=df['TicketGroupSize'].fillna(df['TicketGroupSize'].median())
    df['Cabin'].nunique()
    df['Deck']=df['Cabin'].str[0]
    df['Deck'].nunique()
    df['Deck']=df['Deck'].fillna('Unkown')
    df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
    df.drop(['Cabin','Name','Ticket'],axis=1,inplace=True)
    return df