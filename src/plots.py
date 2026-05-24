import matplotlib.pyplot as plt

# Visualize the cumulative revenue percentage to show the Pareto distribution
def plot_pareto_sales(df):
    plt.figure(figsize=(14, 6))

    plt.plot(
        range(1, len(df) + 1),
        df["cum_pct"],
        linestyle="-",
        color="blue",
        linewidth=2
    )

    plt.axhline(
        y=0.8,
        color="red",
        linestyle="--",
        label="80% Revenue Threshold"
    )

    plt.title("Pareto Revenue Concentration Across Products")
    plt.xlabel("Number of Products")
    plt.ylabel("Cumulative Revenue Percentage")
    plt.xlim(0, len(df))
    plt.ylim(0, 1.05)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()

# Plot the weekly sales comparison
def plot_weekly_sales_comparison(*args):
    plt.figure(figsize=(14, 6))
    
    for sales_data, label in args:
        plt.plot(sales_data["InvoiceDate"], sales_data["Revenue"], label=label, marker='o', markersize=4, alpha=0.7, color=["blue", "red", "green"][len(plt.gca().lines) % 3])
    
    plt.title("Weekly Revenue Comparison")
    plt.xlabel("Sales Date")
    plt.ylabel("Total Revenue")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

# Visualize the weekly sales along with rolling mean and standard deviation for a specific SKU
def plot_weekly_sales_with_rolling_stats(sku_weekly_sales, sku_name, title_suffix=""):
    plt.figure(figsize=(10, 5))
    
    plt.plot(
        sku_weekly_sales["InvoiceDate"], 
        sku_weekly_sales["Quantity"],
        marker="",
        color="blue",
        linestyle="-",
        label="Weekly Sales"
    )
    
    plt.plot(
        sku_weekly_sales["InvoiceDate"], 
        sku_weekly_sales["rolling_mean_4w"],
        color="orange",
        linestyle="-",
        label="4-Week Rolling Mean"
    )
    
    plt.plot(
        sku_weekly_sales["InvoiceDate"], 
        sku_weekly_sales["rolling_std_4w"],
        color="green",
        linestyle="-",
        label="4-Week Rolling Std"
    )
    
    plt.xlabel("Invoice Date")
    plt.ylabel("Quantity")
    plt.title(f"SKU Sales for {sku_name} {title_suffix}")
    plt.legend()
    plt.show()

# Visualize the comparison of WAPE scores across different forecasting models
def plot_model_comparison(models, wape_scores):
    plt.figure(figsize=(12, 6))
    
    plt.bar(models, wape_scores, color=["skyblue", "salmon", "lightgreen", "purple"])
    plt.xlabel("Model")
    plt.ylabel("WAPE (%)")
    plt.title("Forecast Model Benchmark Comparison")
    plt.ylim(0, max(wape_scores) * 1.2)
    
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    for i, score in enumerate(wape_scores):
        plt.text(i, score + 0.5, f"{score:.2f}%", ha="center", va="bottom")
    
    plt.tight_layout()
    plt.show()
