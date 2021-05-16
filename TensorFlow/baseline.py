import os
os.chdir("..")
from utils import ROOT_DIR
import pandas as pd

# read data
data_path = ROOT_DIR + '/data/Historico acciones.xlsx'
df = pd.read_excel(data_path)
