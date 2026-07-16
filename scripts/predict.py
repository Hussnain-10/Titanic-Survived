import pickle 
with open('Random_forest1.pkl', 'rb') as file:
    model=pickle.load(file)
predicted=[[
    1,               #PassengerId	                    
    3,               #Pclass
    1,               #Sex
    22,              #Age
    1,               #SibSp
    0,               #Parch
    7,               #Fare
    2,               #Emkedbar
    0,               #Title
    1,               #TicketGroupSize
    0                #Deck
    
]]
prediction=model.predict(predicted)

print(prediction)
# now its answer is zero model predicted is correct 