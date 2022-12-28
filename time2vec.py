import json
import numpy as np
import math

def num2vec(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    sign = 1 if num > 0 else -1
    num = abs(num)
    for i in range(vec_size):
        vec[i] = (int(num) % 10) * sign / 10
        num = num * 10
    return vec

def num2vec2(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    vec[7] = num
    return vec

def num2vec3(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    sign = 1 if num > 0 else -1
    vec[0] = sign
    num = abs(num)
    for i in range(1,vec_size):
        vec[i] = (int(num) % 10) / 10
        num = num * 10
    return vec

def num2vec_pow(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    vec[0] = num
    vec[1] = num**2
    vec[2] = num**3
    vec[3] = num**5
    vec[4] = num**7
    vec[5] = num**11
    vec[6] = num**13
    vec[7] = num**17
    return vec

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

print(len(vec_data[0]))#fork 0 (3000 vectors)
print(data[0][1])#fork 0 (3000 vectors)


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