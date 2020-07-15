import numpy as np
import pandas as pd
1、temp = data[['XXXXXX']]
   temp.head()
2、temp.head(10)
3、temp = data[['id']]
   temp.head()
4、temp['id'].count()
5、temp[(temp['id']<1000) & (temp['age']>30)]
6、temp.groupby('id').agg({'id':np.size,'order_id':temp['order_id'].drop_duplicates().count()})
7、pd.merge(t1,t2,on='id')
8、pd.concat([table1,table2]).drop_duplicates()
9、table1.ix[~table1['id']=10]
10、table1.ix[~table1['column_name']]