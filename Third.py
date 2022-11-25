import numpy as np
import h5py
import pandas as pd
from itertools import islice
from collections import Counter
'''
get indicis of lines with geo accession
'''
great_table=pd.read_csv('great_table.csv')
df = pd.read_csv('table.csv')
res=df[df.geo_accession.isin(great_table.geo_accession)].reset_index(drop=False)
indices=res['index']
indices2=[]
for i in indices:
    f=i-1
    indices2.append(f)
'''
create an expression table
'''
'''
mouse = h5py.File('mouse_matrix_v11.h5', "r")
d = mouse['data']
express=d.get('expression')
data=[]
for i in indices2:
    data.append(express[::,i])
expression=pd.DataFrame(data)
expression.to_csv('expression.csv')
'''
with h5py.File('mouse_matrix_v11.h5', 'r') as f:
   data_set = f['data']['expression']
   data=data_set[::,indices2]
   expression = pd.DataFrame(data)
   expression.to_csv('expression.csv')
   f.close()

