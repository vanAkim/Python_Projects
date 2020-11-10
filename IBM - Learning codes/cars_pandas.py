import pandas as pd

url = "https://archive.ics.edu/ml/machine-learning-databases/autos/imports-85.csv"
df = pd.read_csv(url, header = None)

df.describe()