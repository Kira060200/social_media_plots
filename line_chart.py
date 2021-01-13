import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

time_filepath = "./wasted_time_on_social_media.csv"

time_data = pd.read_csv(time_filepath, index_col="Date")

print(time_data.head())
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
sns.lineplot(data=time_data['Total'])
plt.xticks(
    rotation=45,
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-small'
)

plt.ylabel('Minutes')
# plt.show()
plt.savefig("total_wasted_time.png", bbox_inches='tight', dpi = 300)

