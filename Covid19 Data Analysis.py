#import modules
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')

#import dataset
corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
df = corona_dataset_csv.drop(["Lat", "Long"], axis = 1)

#Aggregating the rows by country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()

#visualizing data
corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()
corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['China'].diff().plot()

# find max infection rate for all the countries
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates
corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])

#import dataset 
world_happiness_report = pd.read_csv("Dataset/worldwide_happiness_report.csv")
columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)
world_happiness_report.set_index(['Country or region'],inplace=True)
world_happiness_report.head()

#join the datasets
data = world_happiness_report.join(corona_data).copy()
data.head()
data.corr()

#plotting GDP vs maximum infection rate 
x = data['GDP per capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

#Plotting social support vs max infection rate 
x = data['Social support']
y = data['max infection rate']
sns.scatterplot(x,np.log(y)
sns.regplot(x,np.log(y))

#plotting healthy life expectancy vs max infection rate 
x = data['Healthy life expectancy']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

#plotting freedom to make life choices vs max infection rate
x = data['Freedom to make life choices']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
