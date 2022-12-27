import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn import manifold, datasets

n_samples = 101
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)


def num2vec(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    sign = 1 if num > 0 else -1
    num = abs(num)
    for i in range(vec_size):
        vec[i] = (int(num) % 10) * sign / 10
        num = num * 10
    return vec

def add_2d_scatter(ax, points, points_color, title=None):
    x, y = points.T
    # ax.scatter(x, y, c=points_color, s=50, alpha=0.8)
    ax.scatter(x, y, c=points_color, s=50, alpha=0.8)
    ax.set_title(title)
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.yaxis.set_major_formatter(ticker.NullFormatter())

def plot_2d(points, points_color, title):
    fig, ax = plt.subplots(figsize=(3, 3), facecolor="white", constrained_layout=True)
    fig.suptitle(title, size=16)
    add_2d_scatter(ax, points, points_color)
    plt.show()

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


n_neighbors = 12  # neighborhood which is used to recover the locally linear structure
n_components = 2
t_sne = manifold.TSNE(
    n_components=n_components,
    init="random",
    n_iter=5000,
    random_state=0
)

prove = []

for nu in range(50,101):
    prove.append(num2vec(nu/10))

for ni in range(-100,-50):
    prove.append(num2vec(ni/10))

prove = np.array(prove)

print(S_points.shape)
print(S_points[0])
S_t_sne = t_sne.fit_transform(prove)

#plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, alpha=0.8, s=60, marker='o', edgecolors='white')


plot_2d(S_t_sne, S_color, "T-distributed Stochastic  \n Neighbor Embedding")


vec_data[0]
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