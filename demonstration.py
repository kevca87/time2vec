import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
from num2vec import num2vec_matchvie
from num2vec import num2vec_sign
from num2vec import num2vec_1d
from num2vec import num2vec_pow

MIN = -1
MAX = 1
STEP = 0.005

def tsne_demonstration(X,c,plot_title='',n_iter=10000,random_state=0):
    n_components = 2
    t_sne = manifold.TSNE(
        n_components=n_components,
        init="random",
        n_iter=n_iter,
        random_state=random_state
    )
    X_new = t_sne.fit_transform(X)
    #'Spectral'
    #'cool'
    plt.scatter(X_new[:, 0], X_new[:, 1], c=c, cmap='rainbow', alpha=0.8,s=30, marker='o')
    plt.title(plot_title)
    plt.colorbar()
    plt.savefig(f'img/{plot_title}.png')
    plt.show()

#nums = np.concatenate((nums,np.arange(-0.05,0.05,0.0005)))
# nums = np.concatenate((nums,np.arange(0.75,0.95,0.0005)))

if __name__ == '__main__':
    args = {
        #samples generation
        '-min':MIN,
        '-max':MAX,
        '-step':STEP,
        #tsne params
        '-i':10000,
        '-rand':0,
        #num2vec function
        '-f':num2vec_pow
    }

    available_num2vec_functions = {
        'num2vec_pow':num2vec_pow,
        'num2vec_matchvie':num2vec_matchvie,
        'num2vec_sign':num2vec_sign,
        'num2vec_pow':num2vec_pow
    }

    for idx, arg in enumerate(sys.argv):
        if arg == '-f':
            function_name = sys.argv[idx+1]
            args['-f'] = available_num2vec_functions[function_name]
            continue
        if arg in args:
            args[arg] = int(sys.argv[idx+1])
    
    min = args['-min']
    max = args['-max']
    step = args['-step']
    nums = np.arange(min, max+step, step)
    
    num2vec_f = args['-f']
    vectorized_nums = np.array([num2vec_f(num) for num in nums])    
    
    plot_title = f"tsne_demonstration-{num2vec_f.__name__}-i{args['-i']}-rand{args['-rand']}"

    tsne_demonstration(vectorized_nums, nums,plot_title,n_iter=args['-i'],random_state=args['-rand'])