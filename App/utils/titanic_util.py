import pandas as pd
import numpy as np

def tratar(passaggeiro):
    tratado = pd.DataFrame()#pd.DataFrame({'PassengerId': [], 'Pclass':[],'Sex':[], 'Age':[], 'Fare':[], 'Embarked':[], 'Title':[], 'IsAlone':[], 'Age*Class':[]})

    # iniciar
    #tratado['PassengerId'] = passaggeiro['PassengerId']
    tratado['Pclass'] = passaggeiro['Pclass']
    tratado['Age'] = passaggeiro['Age']
    tratado['Embarked'] = passaggeiro['Embarked']
    tratado['Fare'] = passaggeiro['Fare']

    # preenche nulos com medianas
    tratado['Fare'] = tratado['Fare'].fillna(32)
    tratado['Age'] = tratado['Age'].fillna(29)
    tratado['Age'] = tratado['Age'].astype(int)

    # titulo
    tratado['Title'] = passaggeiro.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    tratado['Title'] = tratado['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    tratado['Title'] = tratado['Title'].replace('Mlle', 'Miss')
    tratado['Title'] = tratado['Title'].replace('Ms', 'Miss')
    tratado['Title'] = tratado['Title'].replace('Mme', 'Mrs')
    
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    tratado['Title'] = tratado['Title'].map(title_mapping)
    tratado['Title'] = tratado['Title'].fillna(0)

    # sex
    tratado['Sex'] = passaggeiro['Sex'].map( {'female': 1, 'male': 0} ).astype(int)

    # age
    tratado.loc[ tratado['Age'] <= 16, 'Age'] = 0
    tratado.loc[(tratado['Age'] > 16) & (tratado['Age'] <= 32), 'Age'] = 1
    tratado.loc[(tratado['Age'] > 32) & (tratado['Age'] <= 48), 'Age'] = 2
    tratado.loc[(tratado['Age'] > 48) & (tratado['Age'] <= 64), 'Age'] = 3
    tratado.loc[ tratado['Age'] > 64, 'Age'] = 5

    # IsAlone
    tratado['FamilySize'] = passaggeiro['SibSp'] + passaggeiro['Parch']+1
    tratado['IsAlone'] = 0
    tratado.loc[tratado['FamilySize'] == 1, 'IsAlone'] = 1
    tratado = tratado.drop(['FamilySize'], axis=1)

    # Age*Class
    tratado['Age*Class'] = tratado.Age * tratado.Pclass
    tratado['Age*Class'] = tratado['Age*Class'].astype(int)

    # Embarked
    tratado['Embarked'] = tratado['Embarked'].fillna('S')
    tratado['Embarked'] = tratado['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

    # Fare
    tratado.loc[ tratado['Fare'] <= 7.91, 'Fare'] = 0
    tratado.loc[(tratado['Fare'] > 7.91) & (tratado['Fare'] <= 14.454), 'Fare'] = 1
    tratado.loc[(tratado['Fare'] > 14.454) & (tratado['Fare'] <= 31), 'Fare']   = 2
    tratado.loc[ tratado['Fare'] > 31, 'Fare'] = 3
    tratado['Fare'] = tratado['Fare'].astype(int)

    tratado = tratado[[ 'Pclass','Sex', 'Age', 'Fare', 'Embarked', 'Title', 'IsAlone', 'Age*Class']]

    return tratado

def Tratar_Entrada_Api(entrada):
    passaggeiro = pd.DataFrame(entrada, index=[0])

    tratado = pd.DataFrame()

    tratado['Pclass'] = passaggeiro['Pclass']
    tratado['Age'] = passaggeiro['Age']
    tratado['Embarked'] = passaggeiro['Embarked']
    tratado['Fare'] = passaggeiro['Fare']
    tratado['Title'] = passaggeiro['Title']
    tratado['IsAlone'] = passaggeiro['IsAlone']
    tratado['Sex'] = passaggeiro['Sex']

    # Titulo    
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    tratado['Title'] = tratado['Title'].map(title_mapping)
    tratado['Title'] = tratado['Title'].fillna(0)

    # Age 
    tratado.loc[ tratado['Age'] <= 16, 'Age'] = 0
    tratado.loc[(tratado['Age'] > 16) & (tratado['Age'] <= 32), 'Age'] = 1
    tratado.loc[(tratado['Age'] > 32) & (tratado['Age'] <= 48), 'Age'] = 2
    tratado.loc[(tratado['Age'] > 48) & (tratado['Age'] <= 64), 'Age'] = 3
    tratado.loc[ tratado['Age'] > 64, 'Age'] = 5

    # Fare
    tratado.loc[ tratado['Fare'] <= 7.91, 'Fare'] = 0
    tratado.loc[(tratado['Fare'] > 7.91) & (tratado['Fare'] <= 14.454), 'Fare'] = 1
    tratado.loc[(tratado['Fare'] > 14.454) & (tratado['Fare'] <= 31), 'Fare']   = 2
    tratado.loc[ tratado['Fare'] > 31, 'Fare'] = 3
    tratado['Fare'] = tratado['Fare'].astype(int)

    # Age*Class
    tratado['Age*Class'] = tratado.Age * tratado.Pclass
    tratado['Age*Class'] = tratado['Age*Class'].astype(int)

    tratado = tratado[[ 'Pclass','Sex', 'Age', 'Fare', 'Embarked', 'Title', 'IsAlone', 'Age*Class']]

    return tratado