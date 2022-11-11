import numpy as np
import h5py
import pandas as pd
f = h5py.File('mouse_matrix_v11.h5', "r")
data=f.keys()
for key in f.keys():
    print(key)
for key in f['meta'].keys():
    print(key)
#df = pd.DataFrame(np.array(h5py.File('mouse_matrix_v11.h5')['meta']['samples']['source_name_ch1']))
#print(df)
list_of_columns=f['meta']['samples'].keys()
print(list_of_columns)
with h5py.File('mouse_matrix_v11.h5', 'r') as h5_mouse:
    decoder=np.vectorize(lambda x: x.decode())
    normal_res=decoder(h5_mouse['meta/samples/source_name_ch1'])
print(normal_res)
finder = np. vectorize (lambda X:'T cell' in X)
select_cells=normal_res[finder (normal_res)]
print(len(select_cells))
with h5py.File('mouse_matrix_v11.h5', 'r') as h5_mouse:
    decoder=np.vectorize(lambda x: x.decode())
    normal_res2=decoder(h5_mouse['meta/samples/data_processing'])
print(normal_res2)
finder = np. vectorize (lambda X:'kallisto' in X)
select_kal=normal_res2[finder (normal_res2)]
print(len(select_kal))
'''
with h5py.File('mouse_matrix_v11.h5', 'r') as h5_mouse:
    decoder=np.vectorize(lambda x: x.decode())
    normal_res=decoder(h5_mouse['meta/samples/source_name_ch1'])
print(normal_res)
list_of_columns=f['meta']['samples'].keys()
print(list_of_columns)
for elem in f['meta']['samples']['source_name_ch1']:
   print(elem)
df = pd.DataFrame(np.array(h5py.File('mouse_matrix_v11.h5')['meta']['samples']))

select_content=df[df['source_name_ch1'].str.contains("T cell")]
print(len(select_content))
'''
