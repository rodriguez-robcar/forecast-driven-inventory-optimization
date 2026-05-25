-- DATASET OVERVIEW --
SELECT
  COUNT(*) AS total_records,
  COUNT(DISTINCT InvoiceNo) AS unique_invoice_count,
  COUNT(DISTINCT StockCode) AS unique_product_count,
  COUNT(DISTINCT CustomerID) AS unique_customer_count,
  COUNT(DISTINCT Country) AS unique_country_count,
  ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue,
  MIN(InvoiceDate) AS min_invoice_date,
  MAX(InvoiceDate) AS max_invoice_date
FROM `demand-forecasting-496421.uci_online_retail.online_retail`;

-- REVENUE BY SKU --
SELECT
  StockCode,
  ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM `demand-forecasting-496421.uci_online_retail.online_retail`
WHERE Quantity > 0
GROUP BY StockCode
ORDER BY revenue DESC;

-- WEEKLY SKU DEMAND AGGREGATION --
SELECT
  StockCode,
  DATE_TRUNC(InvoiceDate, WEEK) AS invoice_week,
  SUM(Quantity) AS weekly_quantity,
  ROUND(SUM(Quantity * UnitPrice), 2) AS weekly_revenue
FROM `demand-forecasting-496421.uci_online_retail.online_retail`
WHERE Quantity > 0
GROUP BY 1, 2
ORDER BY 1, 2 DESC;

-- FULLY OBSERVED PRODUCT FILTERING --
SELECT
  StockCode,
  COUNT(DISTINCT DATE_TRUNC(InvoiceDate, WEEK)) AS observed_weeks
FROM `demand-forecasting-496421.uci_online_retail.online_retail`
WHERE Quantity > 0
GROUP BY StockCode
HAVING COUNT(DISTINCT DATE_TRUNC(InvoiceDate, WEEK)) = 53;

-- PARETO SEGMENTATION--
WITH SKU_REVENUE AS (
  SELECT
  StockCode,
  ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
  FROM `demand-forecasting-496421.uci_online_retail.online_retail`
  WHERE Quantity > 0
  GROUP BY StockCode
)

SELECT
  StockCode,
  SUM(revenue) OVER (ORDER BY revenue DESC) / SUM(revenue) OVER () AS cumulative_pct
FROM SKU_REVENUE
ORDER BY revenue DESC;

-- TOP SELLING SKUS BY TOTAL QUANTITY --
SELECT
  StockCode,
  SUM(Quantity) AS total_quantity
FROM `demand-forecasting-496421.uci_online_retail.online_retail`
GROUP BY StockCode
Order BY total_quantity DESC
LIMIT 100;

-- CANCELLED ORDERS (INVOICENO STARTS WITH LETTER 'C') --
SELECT
  COUNT(*) AS records_with_cancelled_orders,
  COUNT(DISTINCT InvoiceNo) AS cancelled_orders,
  ROUND(100 * COUNT(InvoiceNo) / 541909, 2) AS cancellation_ratio
FROM `demand-forecasting-496421.uci_online_retail.online_retail`
WHERE InvoiceNo LIKE 'C%' OR InvoiceNo LIKE 'c%';
