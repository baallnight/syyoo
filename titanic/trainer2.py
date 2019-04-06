import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ctx = "C:/Users/ezen/PycharmProjects/syyoo2/titanic/data/"

train = pd.read_csv(ctx+"train.csv")

test = pd.read_csv(ctx+"test.csv")

# df = pd.DataFrame(train)
# print(df.columns)

"""
'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
고객아이디 PassengerId
생존여부    survival    Survival    0 = No, 1 = Yes
승선권     pclass    Ticket class    1 = 1st, 2 = 2nd, 3 = 3rd
이름      Name
성별      sex    Sex    
나이      Age    Age in years    
형제/자매/배우자   sibsp    # of siblings / spouses aboard the Titanic    
동반한 부모,자식      parch    # of parents / children aboard the Titanic    
티켓번호    ticket    Ticket number    
요금      fare    Passenger fare    
객실 번호   cabin    Cabin number    
승선 항구명  embarked    Port of Embarkation    C = Cherbourg, Q = Queenstown, S = Southampton


f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'].value_counts().plot.pie(explode=[0, 0, 1], autopct="%1.1f%%", ax=ax[0], shadow=True)

ax[0].set_title('Survived')
ax[0].set_ylabel('')

sns.countplot('Survived', data=train, ax=ax[1])
ax[1].set_title('Survived')

plt.show()
exit()


데이터는 훈련데이터(train.csv), 목적데이터(test.csv) 두가지로
제공됩니다.
목적데이터는 위 항목에서는 Survived 정보가 빠져있습니다.
그것은 답이기 때문입니다.

"""

f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'][train["Sex"] == 'male'].value_counts().plot.pie(explode=[0, 0, 1],
                                      autopct="%1.1f%%", ax=ax[0], shadow=True)

train['Survived'][train["Sex"] == 'female'].value_counts().plot.pie(explode=[0, 0, 1],
                                      autopct="%1.1f%%", ax=ax[1], shadow=True)

ax[0].set_title('Survived(Male)')
ax[0].set_ylabel('Survived(Female)')

sns.countplot('Survived', data=train, ax=ax[1])
ax[1].set_title('Survived')

plt.show()

# 남성 생존률 18.9 사망률 81.1%
# 여성 생존률 74.2% 사망률 25.8%

# *******
# 승선권 Pclass
# ******

df_1 = [train['Sex'], train['Survived']]
df_2 = train['Pclass']
pd.crosstab(df_1, df_2, margins=True)
#print(df.head())


"""

"""


f, ax = plt.subplots(2, 2, figsize=(20, 15))
sns.countplot('Embarked', data=train, ax=ax[0,0])
ax[0,0].set_title('No. Of Passengers Boarded')
sns.countplot('Pclass', data=train, ax=ax[0,1])
ax[0,1].set_title('No. Of Passengers Pclass')
sns.countplot('Pclass', data=train, ax=ax[1,0])
ax[1,0].set_title('No. Of Passengers Pclass')
sns.countplot('Pclass', data=train, ax=ax[1,0])
ax[1,1].set_title('No. Of Passengers Pclass')
sns.countplot('Pclass', data=train, ax=ax[1,1])

train['Survived'].value_counts().plot.pie(explode=[0, 0, 1],
                                      autopct="%1.1f%%", ax=ax[0], shadow=True)

ax[0].set_title('Survived')
ax[0].set_ylabel('')

sns.countplot('Survived', data=train, ax=ax[1])
ax[1].set_title('Survived')


#결측치 제거

train.info()

train.isnull().sum()