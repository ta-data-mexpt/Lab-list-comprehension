# %%
import pandas as pd
import os
files_path = ['../data/'+f for f in os.listdir('../data') if f.endswith('.csv')]
df = pd.concat(map(pd.read_csv, files_path))                   
df.head(10)
# %%
# mean of a col
col_mean = df["0"].mean()
print(col_mean)
# %%
list_mean = [ mean for mean in df.mean() if mean > 0.48 ]
list_mean
# %%
col_19 = df["19"] - 0.1
col_19.head(10)
df["20"] = col_19
df.head(10)

# %%
df["20"] = df["19"] - 0.1
df.head(10)
# %%
# dl = [val for val in df.values() if val >0.7 and val<0.75]
# dl = df["0"][df["0"].between(0.7, .75)]
dl = df.values().between(0.7, .75)
dl

# %%
row = next(df.iterrows())[1]
row
# %%
for col in df.columns:
    print(col)
# %%
list(df.columns)
# list(df.columns.values)
# %%
list(df.columns.values.tolist())
# %%
list_range = [val for val in df.columns.values]
list_range
# %%
for i, j in df.iterrows():
    print([i, j])
# %%
# using iteritems() function to retrieve rows
for key, value in df.iteritems():
    # if value > 0.7 and value < 0.75:
        print(key, value)
# %%
# creating a list of dataframe columns
columns = list(df)
for i in columns:
    # if df[i] > 0.7 and df[i] < 0.75:
    print (df[i])
# %%
# Iterate over column names
for index in range(df.shape[1]):
    print('Column Number : ', index)
    columnSeriesObj = df.iloc[:, index]
    print('Column Contents : ', columnSeriesObj.values)
# %%
for column_name in df:
    print(type(column_name))
    print(column_name)
    print('------\n')
# %%
for column_name, item in df.iteritems():
    print(type(column_name))
    print(column_name)
    print('~~~~~~')

    print(type(item))
    print(item)
    print('------')
# %%
df.describe()
# %%
df

# %%
for i, row in df.iterrows():
    while i < 20:
        print(row['0'])
        break

# %%
col = [x for x in df["0"]]
col
# %%
list(df.columns)
# %%
list_values = [val for col in list(df.columns) for val in df[col] if val>0.7 and val<0.75]
list_values
# %%
