# Google Trends Forecasting using Time Series Analysis

This project analyzes and forecasts public interest in various topics using data from **Google Trends**. It focuses on comparing keyword pairs like `"Remote jobs vs Office jobs"` and forecasting future search trends using **Facebook Prophet**, a powerful time series forecasting tool.


## Project Objective

To forecast and visualize public interest trends for selected keyword pairs using **Google Trends API**, **EDA**, and **time series forecasting** techniques.


## Keywords Analyzed

- **Remote jobs** vs **Office jobs** *(Career trends)*
- **Stock market** vs **Cryptocurrency** *(Investment interest)*
- **LinkedIn** vs **Indeed** *(Job platform popularity)*



## Tools & Technologies Used

- **Python**
- **PyTrends** – to access Google Trends data
- **Pandas, NumPy** – data handling & preprocessing
- **Seaborn, Matplotlib** – data visualization
- **Prophet** – time series forecasting
  

## Project Workflow

1. **Data Collection**  
   Fetched real-time keyword pair data from Google Trends using `pytrends`.

2. **Exploratory Data Analysis (EDA)**  
   Used pandas, numpy, seaborn, and matplotlib to visualize keyword trends over time.

3. **Trend Visualization**  
   Plotted line graphs comparing search interest for each keyword pair from 2018 to mid-2025.

4. **Time Series Forecasting**  
   Implemented forecasting models using **Prophet** to predict keyword popularity for the next 365 days.

5. **Evaluation**  
   Compared actual vs predicted trends to analyze forecast quality and pattern consistency.



## Key Highlights

- Implemented **time series analysis** using Prophet to forecast search interest and popularity for individual keywords  
- Visualized trend comparisons to understand behavioral shifts in job search, investing, and work preference  
- Gained insights into **public interest dynamics** using real-world data and statistical forecasting  



## ✅ Outcome

This project demonstrates the ability to apply **data science and machine learning techniques** to real-world public data, generate actionable insights, and predict future behavior trends based on historical interest.
