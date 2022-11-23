import numpy as np
import h5py
import pandas as pd
import re
from itertools import islice
from collections import Counter

df = pd.read_csv('del_single.csv')

'''
Create a table with needing columns - макрофаги
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0) - сложение таблиц
'''

wf = df[['geo_accession', 'platform_id', 'source_name_ch1']] #wf - working frame
macrophage= wf[wf['source_name_ch1'].str.contains('macrophage|macrophages', case=False)]
macrophage.insert(2, "Cell type", 'macrophage')
conditions = [
    (macrophage['source_name_ch1'].str.contains('Bone marrow', case=False)),
    (macrophage['source_name_ch1'].str.contains('Peritoneal', case=False)),
    (macrophage['source_name_ch1'].str.contains('Alveolar', case=False)),
    (macrophage['source_name_ch1'].str.contains('tumor', case=False)),
    (~macrophage['source_name_ch1'].str.contains('Bone marrow derived macrophage|Peritoneal|Alveolar|tumor' , case=False))
]

values = ['Bone Marrow Derived', 'Peritoneal macrophage', 'Alveolar macrophage', 'tumor macrophage', 'other macrophage']
macrophage.insert(3, "Classes", np.select(conditions, values))
macrophage.to_csv('macrophage.csv')

'''
create a table of T-cells
'''
wf = df[['geo_accession', 'platform_id', 'source_name_ch1']] #wf - working frame
T_cells= wf[wf['source_name_ch1'].str.contains('T-cells|T cells|T-cell| T cell| CD8| CD4', case=False)]
T_cells.insert(2, "Cell type", 'T_cells')
conditions = [
    (T_cells['source_name_ch1'].str.contains('CD8[+,\s]',case=False, regex=True)),
    (T_cells['source_name_ch1'].str.contains('CD4[+,\s]',case=False, regex=True)),
    (~T_cells['source_name_ch1'].str.contains('CD8[+,\s]|CD4[+,\s]' , case=False, regex=True))
]
values = ['CD8+ T-cells', 'CD4+ T-cells', 'other T-cells']
T_cells.insert(3, "Classes", np.select(conditions, values))
T_cells.to_csv('T_cells.csv')

'''
create a table of B-cells
'''