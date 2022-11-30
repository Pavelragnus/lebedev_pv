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
macrophage.insert(3, "Cell type", 'macrophage')
conditions = [
    (macrophage['source_name_ch1'].str.contains('[Bm]one(-|\s)marrow', case=False, regex=True)),
    (macrophage['source_name_ch1'].str.contains('Peritoneal', case=False)),
    (macrophage['source_name_ch1'].str.contains('Alveolar|lung', case=False)),
    (macrophage['source_name_ch1'].str.contains('tumor|tumour', case=False)),
    (macrophage['source_name_ch1'].str.contains('Splenic', case=False)),
    (macrophage['source_name_ch1'].str.contains('hepatic', case=False)),
    (macrophage['source_name_ch1'].str.contains('sciatic nerve', case=False)),
    (macrophage['source_name_ch1'].str.contains('Phagocytic', case=False)),
    (macrophage['source_name_ch1'].str.contains('Peripheral', case=False)),
    (macrophage['source_name_ch1'].str.contains('muscle', case=False)),
    (macrophage['source_name_ch1'].str.contains('1 day after TBI', case=False)),
    (~macrophage['source_name_ch1'].str.contains('[Bm]one(-|\s)marrow|Peritoneal|Alveolar|tumor|tumour|Splenic|lung|hepatic|sciatic nerve|Phagocytic|Peripheral|muscle|1 day after TBI' , case=False))
]

values = ['Bone Marrow Derived macrophages', 'Peritoneal macrophage', 'Alveolar macrophage', 'tumor macrophage','Splenic macrophages','hepatic macrophages', 'sciatic nerve macrophages','Phagocytic macrophages', 'Peripheral macrophages','muscle macrophages','1 day after TBI macrophages', 'other macrophage']
macrophage.insert(4, "Classes", np.select(conditions, values))
macrophage.to_csv('macrophage.csv')

'''
create a table of T-cells
'''

T_cells= wf[wf['source_name_ch1'].str.contains('(/s)+T(-|\s)cell(\s|s)|(\s)+CD8(+|\s)(\s)+| (\s)CD4(+|\s)(\s)+', case=False)]
T_cells.insert(3, "Cell type", 'T_cells')
conditions = [
    (T_cells['source_name_ch1'].str.contains('(\s)+CD8(\+|\s)(\s)+',case=False, regex=True)),
    (T_cells['source_name_ch1'].str.contains('(\s)+CD4(+|\s)(\s)+',case=False, regex=True)),
    (T_cells['source_name_ch1'].str.contains('YFP+', case=False, regex=True)),
    (T_cells['source_name_ch1'].str.contains('V\\xce\\xb34', case=False)),
    (T_cells['source_name_ch1'].str.contains('Tumor-infiltrating', case=False)),
    (T_cells['source_name_ch1'].str.contains('Thymus|Thymic', case=False)),
    (T_cells['source_name_ch1'].str.contains('Splenic|spleen', case=False)),
    (~T_cells['source_name_ch1'].str.contains('(\s)+CD8(\+|\s)(\s)+|(\s)+CD4(+|\s)(\s)+|YFP+|V\\xce\\xb34|Tumor-infiltrating|Thymus|Thymic|Splenic|spleen', case=False, regex=True))
]
values = ['CD8+ T cells', 'CD4+ T cells', 'YFP+ T cells','V\xce\xb34 T cell', 'Tumor-infiltrating T cells', 'Thymus T cells', 'Splenic T cells', 'other T cells']
T_cells.insert(4, "Classes", np.select(conditions, values))
T_cells.to_csv('T_cells.csv')

'''
create a table of B-cells
'''

B_cells= wf[wf['source_name_ch1'].str.contains('(\s)+B(-|\s)cell(s|\s)', case=False, regex=True)]
B_cells.insert(3, "Cell type", 'B_cells')
conditions = [
    (B_cells['source_name_ch1'].str.contains('splenic|from spleen|spleenic',case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('Germinal center',case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('Marginal zone' , case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('Follicular|folicular' , case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('B220+' , case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('Primary' , case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('NP+ GC', case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('immature', case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('CH12 ', case=False, regex=True)),
    (B_cells['source_name_ch1'].str.contains('CD19+', case=False, regex=True)),
    (~B_cells['source_name_ch1'].str.contains('splenic|from spleen|spleenic|Germinal center|Marginal zone|Follicular|folicular|B220+|primary|NP+ GC|immature|CH12|CD19+ ' , case=False, regex=True))

]
values = ['splenic B cells', 'Germinal center B cells', 'Marginal zone B cells', 'Follicular B cells', 'B220+ B cells','Primary B cells','NP+ GC B cells','Immature B cells','CH12 line','CD19+ B cells', 'other B-cells']
B_cells.insert(4, "Classes", np.select(conditions, values))
B_cells.to_csv('B_cells.csv')

'''
Concatenate three tables
'''
B_cells=pd.read_csv('B_cells.csv')
T_cells=pd.read_csv('T_cells.csv')
macrophage=pd.read_csv('macrophage.csv')
great_table = pd.concat([B_cells, T_cells, macrophage], axis=0)
great_table = great_table.drop(great_table.columns[[0]], axis = 1)
great_table.to_csv('great_table.csv')