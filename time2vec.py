import json
import numpy as np
import math
from num2vec import num2vec_matchvie
from num2vec import num2vec_sign
from num2vec import num2vec_1d
from num2vec import num2vec_pow

file_name = 'timeseries/eclipse-vertx__vert.x#io.vertx.benchmarks.ContextBenchmark.runOnContextNoChecks#.json'
f = open(file_name)
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
        fork_vecs.append(num2vec(normalized_num,16))
        fork_normalized.append(normalized_num)
    normalized_data.append(fork_normalized)
    vec_data.append(fork_vecs)

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