import matplotlib.pyplot as plt

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

'''
def plot_feature_importance(model, feature_names, top_n=20):
    importance = model.feature_importances_
    feature_importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importance
    }).sort_values(by="importance", ascending=False).head(top_n)
    
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance_df["feature"], feature_importance_df["importance"], color="skyblue")
    plt.xlabel("Importance")
    plt.title("Top Feature Importances")
    plt.gca().invert_yaxis()
    plt.show()
'''