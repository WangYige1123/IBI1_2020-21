import numpy as np
gene_lengths = np.array([9410, 394141, 4442, 105338, 19149, 76779, 126550, 
36296, 842, 15981])
exon_counts = np.array([51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523])
# Get the average exon length across 10 genes
average = gene_lengths/exon_counts
average.sort()
print (average)
import matplotlib.pyplot as plt
# Make some changes to avoid sticking to the default choices
plt.boxplot(average,
            notch = False,
            vert = True,
            whis = 1.5,
            patch_artist = False,
            meanline = True,
            showmeans = True)
plt.show()
         
