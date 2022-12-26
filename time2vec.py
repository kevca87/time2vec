import json
import numpy as np
import matplotlib.pyplot as plt

def num2vec(num,vec_size=8):
    vec = np.zeros(vec_size,np.float)
    sign = 1 if num > 0 else -1
    num = abs(num)
    for i in range(vec_size):
        vec[i] = (int(num) % 10) * sign / 10
        num = num * 10
    return vec


f = open('timeseries/eclipse-vertx__vert.x#io.vertx.benchmarks.ContextBenchmark.runOnContextNoChecks#.json')
data = json.load(f)
normalized_data = []
vec_data = []
for fork_exec_times in data:
    min_exec_time = min(fork_exec_times)
    max_exec_time = max(fork_exec_times)
    X_min = min_exec_time
    X_max = max_exec_time
    fork_normalized = []
    fork_vecs = []
    for X in fork_exec_times:
        normalized_num = (2*(X-X_min)/(X_max-X_min))-1
        fork_vecs.append(num2vec(normalized_num,16))
        fork_normalized.append(normalized_num)
    normalized_data.append(fork_normalized)
    vec_data.append(fork_vecs)

print('min value: ',min(data[0]))
print('max value: ',max(data[0]))
print('x:            ',data[0][1])
print('x normalized: ',normalized_data[0][1])
print('x vectorized: ',vec_data[0][1])
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(normalized_data[0])
 
# show plot
plt.show()

# domain [-1,1]

# print(num2vec(1.0000))
# print(num2vec(0.9513))
# print(num2vec(-0.9513))