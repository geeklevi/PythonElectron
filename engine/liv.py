import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys, json

#tutorial:
# https://ourcodeworld.com/articles/read/286/how-to-execute-a-python-script-and-retrieve-output-data-and-errors-in-node-js

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# def run_script(dt):
#     print(dt)

# line = sys.stdin.readline()
# print(line)
# print(line[0])
# run_script("haha")


# simple JSON echo script
for line in sys.stdin:
  print(json.dumps(json.loads(line)))

# for v in sys.argv[1:]:
#   print(v)