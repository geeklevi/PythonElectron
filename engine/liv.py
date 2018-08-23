import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

# def run_script(dt):
#     print(dt)

# line = sys.stdin.readline()
# print(line)
# run_script("haha")