import numpy as np
from matplotlib import ticker
from time2vec import num2vec
from time2vec import num2vec2
from time2vec import num2vec3
from time2vec import num2vec_pow
import matplotlib
import matplotlib.pyplot as plt
# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn import manifold, datasets


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

n_neighbors = 12  # neighborhood which is used to recover the locally linear structure
n_components = 2
t_sne = manifold.TSNE(
    n_components=n_components,
    init="random",
    n_iter=10000,
    random_state=0
)

nums = np.arange(-1,1.005,0.005)

# nums = np.arange(-0.95,-0.75,0.0005)
# nums = np.concatenate((nums,np.arange(-0.05,0.05,0.0005)))
# nums = np.concatenate((nums,np.arange(0.75,0.95,0.0005)))
print(nums)
print(nums.shape)


vectorized_nums = []
n_samples = nums.shape[0]
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)
color = []

cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=-1, vmax=1)

for num in nums:
    vectorized_num = num2vec_pow(num)
    vectorized_nums.append(vectorized_num)
    if num > 0:
        color.append(1)
    else:
        color.append(-1)
    print(num,' ',vectorized_num)

color = np.array(color)
print(S_color.shape)
print(color.shape)

# for nu in range(50,101):
#     vectorized_nums.append(num2vec(nu/10))

# for ni in range(-100,-50):
#     vectorized_nums.append(num2vec(ni/10))


# print(S_points.shape)
# print(S_points[0])
S_t_sne = t_sne.fit_transform(vectorized_nums)


#plt.scatter(S_t_sne[:, 0], S_t_sne[:, 1], c=nums, cmap='Spectral', alpha=0.8,s=60, marker='o', edgecolors='white')
# plt.scatter(S_t_sne[:, 0], S_t_sne[:, 1], c=nums, cmap='cool', alpha=0.8,s=30, marker='o', edgecolors='white')
plt.scatter(S_t_sne[:, 0], S_t_sne[:, 1], c=nums, cmap='rainbow', alpha=0.8,s=30, marker='o')
plt.colorbar()
plt.show()
#plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, alpha=0.8, s=60, marker='o', edgecolors='white')


# plot_2d(S_t_sne, S_color, "T-distributed Stochastic  \n Neighbor Embedding")