import pandas as pd
from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
print(cancer.feature_names)
print(cancer.target_names)
df=pd.DataFrame(cancer.data, columns=cancer.feature_names)
print(df.head())
df['target']=cancer.target
print(df.head)
print(df[df.target==1].head()) #assigning levels
df['flower_name'] = cancer.target_names[df['target']]
print(df.head())
from sklearn.model_selection import train_test_split
x=df.drop(['target', 'flower_name'],axis='columns')
y=df.target
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2,random_state=1)
print(len(x_train))
print(len(x_test))
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=30)
print(knn.fit(x_train, y_train))
print(knn.score(x_test, y_test))