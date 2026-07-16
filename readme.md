#  Titanic Dataset
Classify the titanic dataset is it save or not ?
## Project Overview
The project is the analyze the titanic Dataset feature and build a model that can the person is save or die.
## Dataset Features
The dataset contain the following features:
- PassengerId
- Bathrooms
- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked
- Title
- TicketGroupSize
- Deck
 Target Variable :
- Survived
## Data Preprocessing
The following preprocessing steps were performed:
- Loaded the dataset
- checked missing values
- Dropped unnecsaary column 
- Change the name in the title for example mr,mrs, miss,dr,
- Change the ticket column into the ticketgroupszie how many people go 
- Remove the class column and make deck for example a calss b class like that
- prepared data for machine learning models
## Machine learning Models
The following regression models were trained and compared
1. Logistic Regression 
2. K-Nearest Neighbors Classifier
3. Decision Tree Classifier
4. Random Forest Classifeir
## Model Evaluation 
Model are evaluated using:
- Accuracy 
- precision  
- recall score
Example Comparison :
MODEL                                Accuracy               |precision                         | recall score
Logistic Regression            0.8044692737430168           |0.782608695652174                 | 0.7297297297297297
KNeighborsClassifier           0.7988826815642458           | 0.8275862068965517               | 0.6486486486486487
DecisionTreeClassifier         0.7821229050279329           | 0.7536231884057971               | 0.7027027027027027
RandomForestClassifier         0.8379888268156425           |0.8333333333333334               |  0.7702702702702703

## Best Model 
Random Forest Classifier was selected as the final model because it provide the best performance