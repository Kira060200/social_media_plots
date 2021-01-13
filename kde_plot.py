import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

time_filepath = "./wasted_time_on_social_media.csv"

time_data = pd.read_csv(time_filepath, index_col="Date")


def kde_plt(c_n):
    fig = sns.kdeplot(data=time_data[c_n], shade=True)
    # plt.yticks(fig.get_yticks().round(decimals = 3), fig.get_yticks() * 100)
    # plt.ylabel('Distribution [%]', fontsize=16)
    #plt.xticks(fig.get_xticks())
    plt.savefig(c_n + ".png", bbox_inches='tight', dpi = 300)
    plt.clf()


kde_plt('Reddit')
kde_plt('Wapp')
kde_plt('Fb')
kde_plt('Chrome')

