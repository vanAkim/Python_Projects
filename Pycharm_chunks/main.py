import pandas as pd
import numpy as np

df = pd.DataFrame({'Mappe': [0,0,0,1,1,2,2],
                   'Valeurs': [1,2,3,5,4,2,5]})             # Création de df avec mapping des valeurs

df['S'] = df.groupby('Mappe')['Valeurs'].transform(np.sum)  # Applique transform() à chaque ensemble des valeurs mappées. Puis stock ces résultats dans la nouvelle colonne 'S'.
df['M'] = df.groupby('Mappe')['Valeurs'].transform(np.mean)
df['V'] = df.groupby('Mappe')['Valeurs'].transform(np.var)

print(df)