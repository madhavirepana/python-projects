#without GUI applications
import pandas as pd
data=pd.read_csv('sample.txt',chunksize=10)

print(data)
for chunk in data:
    print(chunk)