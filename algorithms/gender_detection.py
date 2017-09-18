
from sklearn import tree

# X = [height,weight,feet-size]
X = [[181,80,44],[170,40,43],[160,60,38],[154,54,37],[161,70,40],[190,50,44],[195,65,40],[104,51,30]]
# Y = [lebels]
Y = ['male','female','female','female','male','male','female','male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([120,80,50])

print (prediction)

