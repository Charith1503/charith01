# -*- coding: utf-8 -*-
"""Toyota.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zM6BCgx7BWw7CGFvI_oJ5BOVW2IVd96M
"""

import pandas as pd

from google.colab import files
import pandas as pd

from google.colab import files
uploaded = files.upload()
file_name=list(uploaded.keys())[0]
cars = pd.read_excel(file_name)
cars

cars.shape

cars.info()

cars.corr(numeric_only=True)

cars.dropna(inplace=True)

cars.describe()

cars.isnull()

import seaborn as sns
import matplotlib.pyplot as plt
corr = cars.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm',fmt=".2f",linewidth=0.5)
plt.show()