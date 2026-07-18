import pandas as pd
import pickle
from Step_1_preprocess import clean_data
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

df = clean_data('Titanic-Dataset.csv')

df = pd.get_dummies(df, columns=['Title', 'Deck'], drop_first=True)

sex_encoder = LabelEncoder()
df['Sex'] = sex_encoder.fit_transform(df['Sex'])

embarked_encoder = LabelEncoder()
df['Embarked'] = embarked_encoder.fit_transform(df['Embarked'])

X = df.drop('Survived', axis=1)
y = df['Survived']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y)

model_Rt = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model_Rt.fit(X_train, y_train)
y_pred_Rt = model_Rt.predict(X_test)

print("accuracy_score: ", accuracy_score(y_test, y_pred_Rt))
print("precision_score: ", precision_score(y_test, y_pred_Rt))
print("recall_score: ", recall_score(y_test, y_pred_Rt))
print("confusion_matrix:\n", confusion_matrix(y_test, y_pred_Rt))

cv_scores = cross_val_score(model_Rt, X_scaled, y, cv=5)
print(f"5-fold CV accuracy: {cv_scores.mean():.3f} +/- {cv_scores.std():.3f}")

with open('Random_forest1.pkl', 'wb') as file:
    pickle.dump({'model': model_Rt, 'scaler': scaler, 'columns': X.columns.tolist(),
                 'sex_encoder': sex_encoder, 'embarked_encoder': embarked_encoder}, file)
print("Saved model bundle.")