
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# visualization
import seaborn as sns

# Importing the dataset
social_data = pd.read_csv('Social_Network_Ads.csv')

#describing data
social_data.describe()

#Dropping User ID
social_data = social_data.drop(['User ID'], axis=1)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
social_data_train, social_data_test = train_test_split(social_data, test_size = 0.25, random_state = 0)
combine = [social_data_train, social_data_test]

####Correlating numerical features
g = sns.FacetGrid(social_data_train, col='Purchased')
g.map(plt.hist, 'Age', bins=20)

g = sns.FacetGrid(social_data_train, col='Purchased')
g.map(plt.hist, 'EstimatedSalary', bins=20)

# Encoding categorical data
for dataset in combine:
    dataset['Gender'] = dataset['Gender'].map( {'Female': 1, 'Male': 0} ).astype(int)

X_train=social_data_train.drop('Purchased',axis=1)
Y_train=social_data_train['Purchased']
X_test=social_data_test.drop('Purchased',axis=1)
Y_test=social_data_test['Purchased']

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Fitting Naive Bayes
from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(X_train, Y_train)
nb_pred= nb.predict(X_test)
acc_nb= round(nb.score(X_train, Y_train) * 100, 2)
print("Naive Bayes accuracy is:", acc_nb)

# Fitting SVM to the Training set
from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, Y_train)
svc_pred= svc.predict(X_test)
acc_svc= round(svc.score(X_train, Y_train) * 100, 2)
print("svm accuracy is:", acc_svc)

# Fitting KNN to the Training set
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors= 3)
knn.fit(X_train, Y_train)
knn_pred= knn.predict(X_test)
acc_knn= round(knn.score(X_train, Y_train) * 100, 2)
print("KNN accuracy is:",acc_knn)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cmNb = confusion_matrix(Y_test, nb_pred)
cmSVC = confusion_matrix(Y_test, svc_pred)
cmKnn = confusion_matrix(Y_test, knn_pred)

print("Naive Bayes\n",cmNb)
print("SVC\n",cmSVC)
print("Knn\n",cmKnn)
