import numpy as np
import h5py
import pandas as pd
from itertools import islice
from collections import Counter
'''
get indicis of lines with geo accession
indices[i]=indices[i-1] можно так 
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
with h5py.File('mouse_matrix_v11.h5', 'r') as f:
   data_set = f['data']['expression']
   data=data_set[::,indices2]
   expression = pd.DataFrame(data, columns=indices2)
   expression.to_csv('expression.csv')
   f.close()

'''
with h5py.File('mouse_matrix_v11.h5', 'r') as f:
   data_set = f['data']['expression']
   data=data_set[::,indices2]
   expression = pd.DataFrame(data, columns=indices)
   expression.to_csv('expression3.csv')
   f.close()

