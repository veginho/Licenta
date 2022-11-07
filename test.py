import sklearn
# Import scikit learn
from sklearn import datasets
# Load data
iris= datasets.load_iris()
# Print shape of data to confirm data is loaded
print(iris.data.shape)