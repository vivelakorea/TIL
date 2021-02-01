from matplotlib.colors import ListedColormap
from Perceptron import Perceptron
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                 'machine-learning-databases/iris/iris.data', header=None)
print(df.tail())


y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-virginica', -1, 1)

X = df.iloc[0:100, [0, 2]].values

# plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setonia')
# plt.scatter(X[50:, 0], X[50:, 1], color='blue', marker='x', label='versicolor')

# plt.xlabel('sepal length[cm]')
# plt.ylabel('petal length[cm]')
# plt.legend(loc='upper left')

# plt.show()


ppn = Perceptron(eta=0.1, n_iter=10)

ppn.fit(X, y)

plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of errors')

plt.show()


def plot_decision_regions(X, y, classifier, resolution=0.2):

    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'ligthgreen', 'grey', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(np.array([]))
