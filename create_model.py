import pickle
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
x = iris.data
y = iris.target

tree = DecisionTreeClassifier()
tree.fit(x,y)
pickle.dump(tree, open('./model.pkl', 'wb'))