import json
import os
import pandas as pd
import numpy as np
import math
from num2vec import num2vec_matchvie
from num2vec import num2vec_sign
from num2vec import num2vec_1d
from num2vec import num2vec_pow

def get_files_from(dir):
    return [t.split('.json')[0] for t in os.listdir(dir) if '.json' in t]


def vectorize_data(file_name):
    f = open(f'timeseries/{file_name}.json')
    data = json.load(f)
    normalized_data = []
    vec_data = []
    for fork_exec_times in data:
        X_min = min(fork_exec_times)
        X_max = max(fork_exec_times)
        fork_normalized = []
        fork_vecs = []
        for X in fork_exec_times:
            normalized_num = (2*(X-X_min)/(X_max-X_min))-1
            fork_vecs.append(num2vec_pow(normalized_num).tolist())
            fork_normalized.append(normalized_num)
        normalized_data.append(fork_normalized)
        vec_data.append(fork_vecs)
    
    # vectorized_data_df = pd.DataFrame(vec_data)
    # vectorized_data_df.to_csv(f"timeseries_vectorized/{file_name}.csv")
    jsonString = json.dumps(vec_data)
    jsonFile = open(f"timeseries_vectorized/{file_name}.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

if __name__ == '__main__':
    files_list = get_files_from('timeseries')
    for file_name in files_list:
        vectorize_data(f'{file_name}')
    


# print(len(vec_data[0]))#fork 0 (3000 vectors)
# print(data[0][1])#fork 0 (3000 vectors)


# print('min value: ',min(data[0]))
# print('max value: ',max(data[0]))
# print('x:            ',data[0][1])
# print('x normalized: ',normalized_data[0][1])
# print('x vectorized: ',vec_data[0][1])
# fig = plt.figure(figsize =(10, 7))
 
# # Creating plot
# plt.boxplot(normalized_data[0])
 
# # show plot
# plt.show()

# domain [-1,1]

# print(num2vec(1.0000))
# print(num2vec(0.9513))
# print(num2vec(-0.9513))