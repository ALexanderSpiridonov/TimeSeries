import os
os.chdir("..")

from utils import ROOT_DIR
import pandas as pd
import matplotlib.pyplot as plt

# read data
data_path = ROOT_DIR + '/data/Historico acciones.xlsx'
df = pd.read_excel(data_path)
df = df.sort_values('Date')

# plot data
plt.plot(df['Date'], df['Close price'])
plt.show()