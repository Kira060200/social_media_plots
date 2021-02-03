import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

time_filepath = "./wasted_time_on_social_media.csv"

time_data = pd.read_csv(time_filepath, index_col="Date")

plt.figure(figsize=(10, 5))
sns.lineplot(data=time_data)
plt.xticks(
    rotation=45,
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-small'
)

plt.ylabel('Minutes')
# plt.show()
plt.savefig("wasted_time.png", bbox_inches='tight', dpi = 300)

plt.clf()

time_data['Total'] = time_data['Reddit'] + time_data['Wapp'] + time_data['Fb'] + time_data['Chrome']
plt.figure(figsize=(10, 5))
sns.lineplot(data=time_data['Total'], label="Time wasted per day")
plt.xticks(
    rotation=45,
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-small'
)

plt.ylabel('Minutes')
# plt.show()
plt.axhline(y=50, xmin=-1, xmax=1, color='orange', linestyle='--', lw=2, label="Target time")
plt.axhline(y=time_data['Total'].median(), xmin=-1, xmax=1, color='r', linestyle='--', lw=1, label="Actual median")
# plotting the legend 
plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center') 
plt.savefig("total_wasted_time.png", bbox_inches='tight', dpi = 300)

