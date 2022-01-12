# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)



#Online Retail II excelindeki 2010-2011 verisini okutup oluşturduğunuz dataframe’in kopyasını oluşturalım ve head alalım.
df_ = pd.read_excel("../input/online-retail-ii-data-set-from-ml-repository/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()
df.head()

# Veri setinin betimsel istatistiklerini inceleyelim.
df.describe([0.25,0.75,0.99]).T


#Eşsiz ürün sayımıza bakalım.
df["StockCode"].nunique() # 4070
df["Description"].nunique() # 4223

# En çok sipariş edilen 5 ürünü çoktan aza doğru sıralayalım.
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()