import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

time_filepath = "./wasted_time_on_social_media.csv"

time_data = pd.read_csv(time_filepath, index_col="Date")

print(time_data.head())


def get_m(col):
    return time_data[col].median()


def autopct_format(values):

    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format


arr = [get_m('Reddit'), get_m('Wapp'), get_m('Fb'), get_m('Chrome')]
print(arr)
my_labels = ["Reddit", "Wapp", "Fb", "Chrome"]
plt.pie(arr, labels=my_labels, autopct=autopct_format(arr), colors=['orange', 'green', 'blue', 'yellow'])
plt.title('Median wasted time/day (in minutes)')
# plt.show()
plt.savefig("median_wasted_time.png", dpi=300)
