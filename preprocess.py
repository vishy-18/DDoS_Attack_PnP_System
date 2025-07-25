import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('dataset.csv')
X = df.drop(['label'], axis=1)
y = df['label']

# Encoding categorical data if needed
X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
