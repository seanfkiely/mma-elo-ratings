# MMA ELO Rating System
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import requests
from bs4 import BeautifulSoup

# Load built-in "tips" dataset from seaborn
tips = sns.load_dataset("tips")

# Show first few rows
tips.head()

# %%
# Basic descriptive stats
tips.describe()

# Count of observations by day
tips['day'].value_counts()

# %%
# Scatterplot: total bill vs tip
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("Tip vs. Total Bill by Sex")
plt.show()


