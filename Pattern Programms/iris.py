import pandas as pd
from sklearn.datasets import load_iris 
iris=load_iris()
print(iris.feature_names) #classification task
print(iris.target_names)
df=pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.head())
df['target']=iris.target
print(df.head)
print(df[df.target==1].head()) #assigning levels
df['flower_name'] = iris.target_names[df['target']] #
print(df.head())
df0=df[:50]  #split
df1=df[50:100]
df2=df[100:]
import matplotlib.pyplot as plt #plotting data
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color='green', marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='blue', marker='.')
plt.show()
from sklearn.model_selection import train_test_split #splitting dataset 
x=df.drop(['target', 'flower_name'],axis='columns')
y=df.target
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2,random_state=1)
print(len(x_train))
print(len(x_test))
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=30)
print(knn.fit(x_train, y_train))
print(knn.score(x_test, y_test))