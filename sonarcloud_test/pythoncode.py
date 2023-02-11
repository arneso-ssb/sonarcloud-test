# # This is a heading


import pandas as pd
from pathlib import *

df = pd.read_csv("travel-insurance.csv")
df

df.shape

df.describe(include=object)


