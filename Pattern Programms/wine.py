import pandas as pd
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

wine = load_wine()
print(wine.feature_names)
print(wine.target_names)


df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
print(df.head())

df['wine_class'] = wine.target_names[df['target']]
print(df.head())


df0 = df[df['target'] == 0]  
df1 = df[df['target'] == 1]  
df2 = df[df['target'] == 2]  
plt.xlabel("Alcohol")
plt.ylabel("Malic Acid")
plt.scatter(df0['alcohol'], df0['malic_acid'], color='green', marker='+', label='Class 0')
plt.scatter(df1['alcohol'], df1['malic_acid'], color='blue', marker='.', label='Class 1')
plt.scatter(df2['alcohol'], df2['malic_acid'], color='red', marker='x', label='Class 2')
plt.legend()
plt.show()

x = df.drop(['target', 'wine_class'], axis='columns')
y = df['target']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
print(len(x_train))
print(len(x_test))

knn = KNeighborsClassifier(n_neighbors=30)  
knn.fit(x_train, y_train)


score = knn.score(x_test, y_test)
print("Accuracy:", score)
