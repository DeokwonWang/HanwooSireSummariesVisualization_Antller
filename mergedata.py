import pandas as pd
from datetime import datetime

current_time = datetime.now()

df1 = pd.read_csv("data/kpn_hereditary_ability.csv", encoding="UTF-8")
df2 = pd.read_csv("data/apidata20220711.csv", encoding="UTF-8")

mergeData = pd.merge(df1,df2,left_on='kpn',right_on='kpn')

mergeData.to_csv("data/mergeData"+current_time.strftime('%Y%M%d')+".csv")