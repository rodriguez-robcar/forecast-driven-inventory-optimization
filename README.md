# ${\color{blue}\text{Forecast-Driven Inventory Optimization}}$

A machine learning system for **weekly SKU demand forecasting** and **inventory policy optimization** using the UCI Online Retail dataset. 
The project forecasts demand for high-value retail products and translates forecast uncertainty into actionable replenishment 
recommendations through safety stock and reorder-point modeling.

#

### Business Problem

Retail inventory planning requires balancing two competing risks:
- **Stockouts** → lost sales and poor customer experience
- **Overstocking** → excess holding costs and capital inefficiency
  
Traditional heuristic replenishment rules often fail under volatile demand conditions.

This project builds a **forecast-informed inventory decision framework** that predicts weekly SKU demand and converts those forecasts into operational inventory policy recommendations.

#

### Key Business Questions

**1. Which products drive the majority of revenue?**</br>
Pareto segmentation identifies commercially critical SKUs.

**2. Which high-value products are statiscally forecastable?**</br>
Continuity constraints ensure sufficient historical observations for temporal modeling.

**3. What will weekly demand be for each SKU?**</br>
Gradient-boosted forecasting models predict near-term unit demand.

**4. How much safety stock is required?**</br>
Demand volatility is translated into protective inventory buffers.

**5. When should replenishment occur?**</br>
Forecast-informed reorder points support proactive inventory planning.

#

### Dataset

**Source**: UC Irvine Online Retail Dataset

https://archive.ics.uci.edu/ml/datasets/online+retail

Contains:

- Invoice transactions
- Product identifiers (StockCode)
- Quantities sold
- Unit prices
- Customer identifiers
- Invoice timestamps
- Country information

Transactions: ~541, 000 invoices | Period: Dec 2010 - Dec 2011

#

### Project Workflow

**1. Exploratory Data Analysis**
- Missing-value inspection
- Cancellation filtering
- Revenue concentration analysis
- Weekly demand aggregation
- Pareto revenue segmentation

Result:</br>
**784 products generated ~80% of total revenue**

<img width="1156" height="547" alt="image" src="https://github.com/user-attachments/assets/ab43d0be-e707-4243-915f-18e662cad2a7" />


#

**2. Forecastability Filtering**

Lag-based forecasting requires uninterrumpted historical observations.

Products with insufficient weekly continuity were excluded.

Final modeling universe:</br>
**232 fully observed high-value SKUs**

These retained products preserved broarder catalog demand dynamics while enabling leakage-safe temporal feature engineering.

<img width="1389" height="590" alt="image" src="https://github.com/user-attachments/assets/428aca83-33ae-4169-83e3-c29c5e3a6530" />


#

**3. Feature Engineering**

Temporal demand signals were encoded using:

**Lag features**
- 1-week lag
- 2-week lag
- 4-week lag
- 8-week lag
- 12-week lag

**Rolling Statistics**
- 4-week rolling mean
- 12-week rolling mean
- Rolling coefficient of variation
- Trend ratio

**Seasonal Features**
- Sine/cosine cyclical week encoding
- Q4 indicator
- December indicator
- Days to Christmas

<img width="1015" height="653" alt="image" src="https://github.com/user-attachments/assets/a89397e6-6004-4d99-abeb-3af08faad14f" />


#

**4. Model Benchmarking**

Models evaluated:
- Naive persistence baseline
- XGBoost
- LightGBM
- CatBoost

Evaluation used **chronological holdout validation** on the final 8 weeks.

**Weekly Forecast Accuracy (WAPE)**

| Model | WAPE | Improvement vs Naive |
|-------|----------|----------|
| Naive Baseline | 64.63% | - |
| XGBoost | 58.92% | 8.84% |
| LightGBM | 58.04% | 10.20% |
| CatBoost | 53.29% | 17.54% |

**Final selected model: CatBoost**

CatBoost outperformed alternative gradient-boosting methods by effectively capturing nonlinear interactions between SKU identity and temporal demand behavior.

<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/b0464c95-1a62-480b-94a8-f84fbad6ab7e" />


#

**5. Inventory Policy Optimization**

Forecast outputs were translated into inventory recommendations using classical service-level inventory theory.

**Safety Stock**

Safety Stock = 1.65 * σ(forecast error) * √(lead time)

**Reorder Point**

Reorder Point = Forecast Demand + Safety Stock

This enables forecast-informed replenishment planning under uncertainty.

#

### Project Structure

```

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_inventory_optimization.ipynb
│
├── sql/
│   └── analytical_queries.sql
│
├── src/
│   ├── features.py
│   └── plots.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

#

### Tech Stack

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Scikit-learn` · `CatBoost` · `XGBoost` · `LightGBM` · `SQL`


#

### Business Impact

CatBoost achieved 53% WAPE across 232 high-value SKUs, 
a 18% improvement over naive persistence — translating to 
more precise reorder points at 95% service level.

#

### Future Improvements

Potential extensions:
- Multi-horizon forecasting
- Probabilstic demand intervals
- Cost-based inventory optimization
- Live inventory system integration

