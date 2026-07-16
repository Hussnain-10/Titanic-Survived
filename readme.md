#  Titanic Dataset 🚢
Classify the titanic dataset is it save or not ?
## Project Overview🔎
The project is the analyze the titanic Dataset feature and build a model that can the person is save or die.
## Dataset Features 📄
The dataset contain the following features:
- PassengerId
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
## Data Preprocessing📑
The following preprocessing steps were performed:
- Loaded the dataset
- checked missing values
- Dropped unnecsaary column 
- Change the name in the title for example mr,mrs, miss,dr,
- Change the ticket column into the ticketgroupszie how many people go 
- Remove the class column and make deck for example a calss b class like that
- prepared data for machine learning models
## Machine learning Models🤖
The following regression models were trained and compared
1. Logistic Regression 
2. K-Nearest Neighbors Classifier
3. Decision Tree Classifier
4. Random Forest Classifeir
## Model Evaluation 🪄
​Models are evaluated using **Accuracy**, **Precision**, and **Recall Score**:

| Model | Accuracy | Precision | Recall |
| :--- | :---: | :---: | :---: |
| **Logistic Regression** | 80.4% | 78.3% | 73.0% |
| **K-Neighbors Classifier** | 79.9% | 82.8% | 64.9% |
| **Decision Tree Classifier** | 78.2% | 75.4% | 70.3% |
| **Random Forest Classifier** | **83.8%** | **83.3%** | **77.0%** |

## Best Model ✔️
Random Forest Classifier was selected as the final model because it provide the best performance
