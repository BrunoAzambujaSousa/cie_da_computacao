# questão 1

import statistics

milhoes_meses = [58, 64, 58, 56, 68, 55, 68, 62, 68, 50, 54, 70]

print(sum(milhoes_meses) / len(milhoes_meses))

mediana = statistics.median(milhoes_meses)

print(mediana)

# questão 2 (não consegui fazer)

# import pandas as pd

freq = milhoes_meses[0].value_counts()
total = len(milhoes_meses)
freq_rel = freq / total

print(freq_rel)
