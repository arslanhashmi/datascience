
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()

X = iris.data
y = iris.target
knn = KNeighborsClassifier() # step one initate object of the classifier/algorithm
knn.fit(X,y) #do the training and make the model
y_pred = knn.predict(X) # testing ( here we are doing this on the same data )
print (metrics.accuracy_score(y,y_pred)) # checking the accuracy.