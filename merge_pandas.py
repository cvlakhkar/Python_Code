import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2,3,2,2],
                    'US_GDP_Thousands':[50,55,65,55]},
                   index = [2001,2002,2003,2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2,3,2,2],
                    'US_GDP_Thousands':[50,55,65,55]},
                   index = [2005,2006,2007,2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7,8,9,6],
                    'Low_tier_HPI':[50,52,50,53]},
                   index = [2001,2002,2003,2004])

df4 = pd.DataFrame({'Year':[2001,2002,2003,2004],
                    'Int_rate':[2,3,2,2],
                    'US_GDP_Thousands':[50,55,65,55]})

df5 = pd.DataFrame({'Year':[2001,2003,2004,2005],
                    'Unemployment':[7,8,9,6],
                    'Low_tier_HPI':[50,52,50,53]})


#print pd.merge(df1,df2,on=['HPI','Int_rate','US_GDP_Thousands'])

##Merge:(index does not matter)

merged = pd.merge(df4,df5, on='Year',how='outer')

### how = left merge as per df4, right as per df5 and inner takes intersection or years)

merged.set_index('Year',inplace=True)
print merged

##Join  (index is honoured)
##df1.set_index('HPI',inplace=True)
##df3.set_index('HPI',inplace=True)
##
##joined = df1.join(df3)
##print joined    ### data replication occurs


##concat & append
