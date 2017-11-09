
# coding: utf-8

import pandas as pd
from pandas import Series, DataFrame

#zdefiniowanie zmiennej 'df' pobierającej informacje nt. kursów ze strony NBP na rok 2017
df = pd.read_csv("http://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2017.csv", sep=';', skip_footer=3, engine='python')

print("Dzienny kurs 'dolara amerykańskiego', 'euro' i 'franka szwajcarskiego' za ostatnie 3 dni")
kurs3 = DataFrame(df, columns=["data","1EUR", "1USD", "1CHF"]).tail(3)
print(kurs3)
print("Pokazuje sume wybranych walut")
print(kurs3.sum())

print("Pokazuje ilość wierszy dla Euro, dolara i franka")
kurs4 = DataFrame(df, columns=["1EUR", "1USD", "1CHF"])
print(kurs4.count())