import pandas as pd
import pickle

with open('Random_forest1.pkl', 'rb') as file:
    bundle = pickle.load(file)
model = bundle['model']
scaler = bundle['scaler']
columns = bundle['columns']
sex_encoder = bundle['sex_encoder']
embarked_encoder = bundle['embarked_encoder']

new_passenger = pd.DataFrame([{
    'Pclass': 3,
    'Sex': 'male',
    'Age': 22,
    'SibSp': 1,
    'Parch': 0,
    'Fare': 7.25,
    'Embarked': 'S',
    'TicketGroupSize': 1,
    'Title': 'Mr',
    'Deck': 'Unkown'
}])

new_passenger = pd.get_dummies(new_passenger, columns=['Title', 'Deck'])
new_passenger['Sex'] = sex_encoder.transform(new_passenger['Sex'])
new_passenger['Embarked'] = embarked_encoder.transform(new_passenger['Embarked'])

new_passenger = new_passenger.reindex(columns=columns, fill_value=0)
new_scaled = scaler.transform(new_passenger)

prediction = model.predict(new_scaled)
print("Predicted Survived:", prediction[0])
