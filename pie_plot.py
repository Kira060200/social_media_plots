import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

time_filepath = "./wasted_time_on_social_media.csv"

time_data = pd.read_csv(time_filepath, index_col="Date")

print(time_data.head())


def get_avg(col):
    return time_data[col].mean()


def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format


arr = [get_avg('Reddit'), get_avg('Wapp'), get_avg('Fb'), get_avg('Chrome')]
print(arr)
my_labels = ["Reddit", "Wapp", "Fb", "Chrome"]
plt.pie(arr, labels=my_labels, autopct=autopct_format(arr), colors=['orange', 'green', 'blue', 'yellow'])
plt.title('Mean wasted time/day (in minutes)')
# plt.show()
plt.savefig("average_wasted_time.png", dpi=300)
