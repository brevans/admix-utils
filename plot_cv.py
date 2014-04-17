#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_table('cv.txt', sep=' ', header=None)

plt.figure(figsize=(12, 6))
df[1].plot(xlim=(0,df.shape[0]-1), marker="o", color="#00526D")
plt.xlabel('K', fontsize=16)
plt.ylabel('CV Error', fontsize=16)
plt.xticks(np.arange(df.shape[0]), df[0])
plt.grid()
plt.show()
