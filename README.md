# time2vec
## Requirements
```
pip install -r requirements.txt
```
## num2vec function demonstration
Run tsne demonstration: plot a serie of values vectorized by the function num2vec and passed to the tool T-distributed Stochastic Neighbor Embedding (to visualize the relationship between high-dimensional data). 
```
python demonstration.py
```
Default function `num2vec_pow` \
Default serie of values $[-1,1]$ \
Default step to generate values in range $0.005$ \
Default tsne iters $10000$ \

### Script arguments
Example
```
python demonstration.py -f num2vec_1d
```
#### num2vec function selection
- `-f <func_name>` name of the function to test, available options `num2vec_pow`, `num2vec_matchvie`, `num2vec_sign`, `num2vec_1d`
#### Nums domain arguments
- `-min <min>` min value of the serie 
- `-max <max>` max value of the serie
- `-step <step>` step to generate values in range
#### TSNE arguments
- `-i <tsne_iters>` tsne iters
- `-rand <random_state>` random_state 