import pandas as pd 
import numpy as np

# Creating empty series 
ser = pd.Series() 
print("Pandas Series: ", ser) 

# simple array 
data = np.array(['g', 'e', 'e', 'k', 's']) 

ser = pd.Series(data) 
print("Pandas Series:\n",ser)


lst = ["geeks",'for','geeks','is','portal','for','geeks']

df = pd.DataFrame(lst)
print(df)


data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
  
  
# accessing a element using index element
print(ser[16])