from utilities import read_property_transactions_for_ward

import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["figure.figsize"] = (20.0, 7.5)
matplotlib.rcParams["font.size"] = 16
matplotlib.pyplot.style.use("ggplot")


ward_name = "Muswell Hill"

property_transactions = read_property_transactions_for_ward(ward_name)

monthly_prices = property_transactions.groupby(
    pd.Grouper(key="transaction_transfer_date", freq="M")
)
monthly_prices_medians = monthly_prices.agg(
    {"transaction_price": ["median"]}
)

yearly_transactions = property_transactions.groupby(
    pd.Grouper(key="transaction_transfer_date", freq="Y")
)
yearly_transactions_counts = yearly_transactions.agg(
    {"transaction_id": ["count"]}
)

fig, axes = plt.subplots(nrows=1, ncols=2)

monthly_prices_medians.plot(title=f"Median Price in {ward_name}", ax=axes[0])
monthly_prices_medians.resample("3M").mean().plot(lw=4, ax=axes[0])
axes[0].set_xlabel("Transaction Date")
axes[0].set_ylabel("Transaction Price (GBP)")
axes[0].legend(["Monthly Values", "3M Rolling Average"])

yearly_transactions_counts.plot.bar(
    title=f"Yearly Transactions in {ward_name}", ax=axes[1], legend=None
)
axes[1].set_xlabel("Transaction Year")
axes[1].set_ylabel("Number of Transactions")
axes[1].set_xticklabels(yearly_transactions_counts.index.year)

fig.savefig(f"{ward_name}.png")
