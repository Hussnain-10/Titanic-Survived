from preprocessr import clean_data
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix
df=clean_data(r'C:\Users\DELL\AppData\Local\Temp\cfe74fc2-ddcb-41c4-baf0-d0d2389d7a09_archive (2).zip.a09\Titanic-Dataset.csv')
OE=OneHotEncoder()
df['Title']=OE.fit_transform(df[['Title']]).toarray()
df['Deck']=OE.fit_transform(df[['Deck']]).toarray()
lE=LabelEncoder()
df['Sex']=lE.fit_transform(df['Sex'])
df['Embarked']=lE.fit_transform(df['Embarked'])
X=df.drop('Survived',axis=1)
y=df['Survived']
scaler=MinMaxScaler()
X_scaled=scaler.fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=42)
model_Rt=RandomForestClassifier(n_estimators=100,random_state=42,class_weight='balanced')
model_Rt.fit(X_train,y_train)
y_pred_Rt=model_Rt.predict(X_test)
print("accuracy_score: ",accuracy_score(y_test,y_pred_Rt))
print("precision_score: ",precision_score(y_test,y_pred_Rt))
print("recall_score: ",recall_score(y_test,y_pred_Rt))
print("confusion_matrix: ",confusion_matrix(y_test,y_pred_Rt))
with open ('Random_forest1.pkl','wb') as file:
    pickle.dump(model_Rt,file)