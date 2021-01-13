import calplot
import numpy as np; np.random.seed(sum(map(ord, 'calplot')))
import pandas as pd
import matplotlib.pyplot as plt

time_filepath = "./wasted_time_on_social_media.csv"

time_data = pd.read_csv(time_filepath, index_col="Date")

all_days = pd.date_range('25/12/2020', periods=365, freq='D')
days = np.random.choice(all_days, 500)
# events = pd.Series(np.random.randn(len(days)), index=days)
#events = pd.Series(time_data['Reddit'], index=time_data['Date'])
time_data['DateTime'] = pd.to_datetime(time_data.index, format='%d-%m-%Y')
# print(time_data['DateTime'])
time_data['Total'] = time_data['Reddit'] + time_data['Wapp'] + time_data['Fb'] + time_data['Chrome']
events = time_data.set_index('DateTime')['Total']
#print(events)
calplot.calplot(events, cmap='YlOrRd')
plt.savefig("cal_heatmap.png", bbox_inches='tight', dpi = 300)
plt.clf()
