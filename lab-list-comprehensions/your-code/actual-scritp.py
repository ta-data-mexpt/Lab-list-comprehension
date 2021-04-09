
# %%
msg = "Hello world"
print(msg)
# ##
# %%
msg = "Hola Mundo"
print(msg)
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sample_file_0.csv")
df.head(10)
plt.plot(df)

# %%
