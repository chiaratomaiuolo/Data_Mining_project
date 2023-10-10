import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# import dataset
df = pd.read_csv("dataset (missing + split)/train.csv", skipinitialspace=True)
cols = ['valence', 'tempo']

#df[cols].mean()
#print(df)
'''
feature = 'danceability'
for v in df['genre'].unique():
    plt.hist(df[df['genre'] == v][feature], 
             bins=np.arange(0., 1., 0.05),
             label=v,
             alpha=0.6
            )
plt.title(feature)
plt.legend()
'''

pd.plotting.scatter_matrix(df,figsize=(8,8))
plt.show()