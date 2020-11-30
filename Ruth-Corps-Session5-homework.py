# The homework exercise for this class is to use the data you collected from your experiment and to explore it, possibly clean it, 
# and plot the main contrast of interest in a sensible way. This applies to both the picture verification task (e.g. matching vs. 
# nonmatching) and the lexical decision task (e.g. word frequency). In case you did not manage to finish the experiment or collect
# data, you can take a look at our example solutions, which also contain some data to use in your analysis

import pandas as pd 
import numpy as np 
import plotnine as gg
from matplotlib import pyplot as plt

# read data
data = pd.read_csv("session5/lexdec_results.csv")
print(data)

# rename the unnamed column 
data = data.rename(columns={'Unnamed: 0': 'trial_order'})

# calculate the means for the columns of interest
summary = data.groupby(by='frequency').aggregate(
    mean_RT=pd.NamedAgg('reaction_time', np.mean),
    std_RT=pd.NamedAgg('reaction_time', np.std), 
    mean_acc=pd.NamedAgg('accuracy', np.mean),
    std_acc=pd.NamedAgg('accuracy', np.std)
)

summary.reset_index(inplace=True)

# plot the reaction times 
plt.figure()
plt.bar(summary['frequency'], summary['mean_RT'])
plt.errorbar(summary['frequency'], summary['mean_RT'], summary['std_RT'], fmt='.k')
plt.suptitle('Reaction Times')
plt.xlabel('Word Frequency')
plt.ylabel('Reaction Time (s)')
plt.show()

# plot the accuracy 
plt.figure()
plt.bar(summary['frequency'], summary['mean_acc'])
plt.errorbar(summary['frequency'], summary['mean_acc'], summary['std_RT'], fmt='.k')
plt.suptitle('Accuracy')
plt.xlabel('Word Frequency')
plt.ylabel('Accuracy (proportion)')
plt.show()


