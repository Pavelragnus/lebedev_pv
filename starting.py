import numpy as np
import h5py
import pandas as pd
from itertools import islice
from collections import Counter

mouse = h5py.File('mouse_matrix_v11.h5', "r") # fot reading h5 dataframe
data=mouse.keys()
for key in mouse.keys():
    print(key)
for key in mouse['meta'].keys():
    print(key)
list_of_columns=mouse['meta']['samples'].keys()
print(list_of_columns)


'''
Now every dataset from h5 file we transform into single table in pandas and then concatenate them into one table
'''
title=mouse['meta']['samples']['title']
title_data=pd.DataFrame(title, columns=['title'])
type=mouse['meta']['samples']['type']
type_data=pd.DataFrame(type, columns=['type'])
geo_accession=mouse['meta']['samples']['geo_accession']
geo_accession_data=pd.DataFrame(geo_accession, columns=['geo_accession'])
data_processing=mouse['meta']['samples']['data_processing']
data_processing_data=pd.DataFrame(data_processing, columns=['data_processing'])
characteristics_ch1=mouse['meta']['samples']['characteristics_ch1']
characteristics_ch1_data=pd.DataFrame(characteristics_ch1, columns=['characteristics_ch1'])
extract_protocol_ch1=mouse['meta']['samples']['extract_protocol_ch1']
extract_protocol_ch1_data=pd.DataFrame(extract_protocol_ch1, columns=['extract_protocol_ch1'])
instrument_model=mouse['meta']['samples']['instrument_model']
instrument_model_data=pd.DataFrame(instrument_model, columns=['instrument_model'])
library_selection=mouse['meta']['samples']['library_selection']
library_selection_data=pd.DataFrame(library_selection, columns=['library_selection'])
library_source=mouse['meta']['samples']['library_source']
library_source_data=pd.DataFrame(library_source, columns=['library_source'])
library_strategy=mouse['meta']['samples']['library_strategy']
library_strategy_data=pd.DataFrame(library_strategy, columns=['library_strategy'])
molecule_ch1=mouse['meta']['samples']['molecule_ch1']
molecule_ch1_data=pd.DataFrame(molecule_ch1, columns=['molecule_ch1'])
organism_ch1=mouse['meta']['samples']['organism_ch1']
organism_ch1_data=pd.DataFrame(organism_ch1, columns=['organism_ch1'])
platform_id=mouse['meta']['samples']['platform_id']
platform_id_data=pd.DataFrame(platform_id, columns=['platform_id'])
readsaligned=mouse['meta']['samples']['readsaligned']
readsaligned_data=pd.DataFrame(readsaligned, columns=['readsaligned'])
readstotal=mouse['meta']['samples']['readstotal']
readstotal_data=pd.DataFrame(readstotal, columns=['readstotal'])
relation=mouse['meta']['samples']['relation']
relation_data=pd.DataFrame(relation, columns=['relation'])
series_id=mouse['meta']['samples']['series_id']
series_id_data=pd.DataFrame(series_id, columns=['series_id'])
source_name_ch1=mouse['meta']['samples']['source_name_ch1']
source_name_ch1_data=pd.DataFrame(source_name_ch1, columns=['source_name_ch1'])
status=mouse['meta']['samples']['status']
status_data=pd.DataFrame(status, columns=['status'])
taxid_ch1=mouse['meta']['samples']['taxid_ch1']
taxid_ch1_data=pd.DataFrame(taxid_ch1, columns=['taxid_ch1'])
table=pd.concat([taxid_ch1_data,status_data,source_name_ch1_data,series_id_data,relation_data,readstotal_data,readsaligned_data,platform_id_data,organism_ch1_data, molecule_ch1_data,library_strategy_data,library_selection_data, library_source_data,instrument_model_data,extract_protocol_ch1_data, characteristics_ch1_data,data_processing_data,geo_accession_data,type_data,title_data ],sort=False, axis=1)
'''
Let's delete rows with words - single cell in a column 'source_name_ch1'
'''
table.to_csv('table.csv') # create a file .csv with our table
df = pd.read_csv('table.csv') # read table into pandas dataframe
discard=["single cell"]
del_single=df[~df.source_name_ch1.str.contains('|'.join(discard))]
del_single.to_csv('del_single.csv')
'''
Create a table with uniqe values
'''
df = pd.read_csv('del_single.csv')
cell_count=df.groupby('source_name_ch1')['platform_id'].value_counts() #count on two column basis
#cell_count=df['source_name_ch1'].value_counts() #create a table with count of uniq cell types
cell_count.to_csv('cell_count.csv') # put table into file .csv

#contain_kal = df[df['data_processing'].str.contains('allisto')]
#contain_kal.to_csv('contain_kal.csv')
#df = pd.read_csv('contain_kal.csv')
#print(len(df))
#contain_cell= df[df['source_name_ch1'].str.contains('Innate lymphoid cell')]
#contain_kalcell.to_csv('contain_kallisto_cell.csv')
#df = pd.read_csv('contain_kallisto_cell.csv')
#print(df)