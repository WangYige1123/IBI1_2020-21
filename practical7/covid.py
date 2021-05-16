import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
covid_data = pd.read_csv("full_data.csv")
covid_data.iloc[0:12:2,:]
Afghanistan_total_cases = covid_data.loc[covid_data['location']=='Afghanistan',
'total_cases']
print(Afghanistan_total_cases)
world_new_cases = covid_data.loc[covid_data['location']=='World','new_cases']
world_new_cases.mean()
world_new_cases.median()
plt.boxplot(world_new_cases,
            vert = True,
            meanline = True,
            whis = 1.5,
            showbox = True,
            vert = True,
            patch_artist = True,
            notch = True)
plt.show()
world_dates = covid_data.loc[covid_data['location']=='World','dates']
world_new_deaths = covid_data.loc[covid_data['location']=='World','new_deaths']
plt.plot(world_dates,world_new_cases,'y',world_dates,world_new_deaths,'g')
plt.show()
Austria_dates = covid_data.loc[covid_data['location']=='Austria','dates']
Austria_new_cases = covid_data.loc[covid_data['location']=='Austria',
'new_cases']
plt.plot(Austria_dates,Austria_new_cases,'y')
plt.show()
