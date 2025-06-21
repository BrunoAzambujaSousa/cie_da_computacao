comprimento = [3, 5, 6, 8, 7, 3]
print(comprimento)

import statistics

variancia = statistics.variance(comprimento)
print(variancia)

desvio_padrao = statistics.stdev(comprimento)
print(desvio_padrao)

import numpy as np

amplitude = np.ptp(comprimento)
print(amplitude)

q1, q2, q3 = np.percentile(comprimento, [25, 50, 75])
print(q1)
print(q2)
print(q3)

from sklearn.datasets import fetch_california_housing
import pandas as pd

california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df.head()