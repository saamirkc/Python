import pandas as pd
foo=pd.Series(['a','b','c','d'],dtype="string")
print(foo)
bar=foo.loc[foo<='b']   # acts as copy
print(bar)

bar.iloc[0]='z'
print(bar)

print(foo)
# here change in index 0  in bar doesnt result in change in index 0 of foo 
# under the hood copy is done 

# in order to use as assignment operator so that change in index 0 in bar 
# result in change in index 0 in foo we can do :

bar=foo.iloc[:2]
print (bar)

bar.iloc[0]='z'
print(bar)

print(foo)

