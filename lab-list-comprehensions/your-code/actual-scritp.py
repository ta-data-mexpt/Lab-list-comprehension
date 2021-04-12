
# %%
msg = "Hello world"
print(msg)
# ##
# %%
msg = "Hola Mundo"
print(msg)
# %%
import pandas as pd
df = pd.read_csv("../data/sample_file_0.csv")
df.head(10)

# %%
import os
csv_files = [csv_file for csv_file in listdir("../data")
#csv_files = [ filename for filename in filenames if filename.endswith(".csv") ]
# %%
