##Step1 import libraries
from pytrends.request import TrendReq   # PyTrends is an unofficial Google Trends API
import pandas as pd           # For data manipulation
import matplotlib.pyplot as plt    # For plotting graphs
import seaborn as sns
from prophet import Prophet        # For time series forecasting

##Step2 fetch data from gogle trend
# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define keyword pairs
keyword_pairs = [
    
    ['Remote jobs', 'Office jobs'],           #carrer shift trend
    ['Stock market', 'Cryptocurrency'],       #Investment Intrest
    ['LinkedIn','Indeed']                     #job search platform popularity
]

#collect trend data for each keyword pair from 2018 to 2025
trend_data = {}          #Create a dictionary to store data for each pair

for pair in keyword_pairs:
    pytrends.build_payload(pair, timeframe='2018-01-01 2025-07-01')
    data = pytrends.interest_over_time().drop(columns='isPartial').reset_index()
    trend_data[' vs '.join(pair)] = data     # Store it with label like "Remote jobs vs On-site jobs"
#display data
data.head()


##Step3 Plot the Search Trends Over Time
for label, df in trend_data.items():        # For each pair, show how interest changed over time
    plt.figure(figsize=(14, 5))
    for col in df.columns[1:]:
        sns.lineplot(data=df, x='date', y=col, label=col)
    plt.title(f'Trend Comparison: {label}')
    plt.xlabel('Date')
    plt.ylabel('Search Interest')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


##Step4 forecast keywords
def forecast_keyword(df, keyword): #Define Prophet Forecasting Function
    """"
    This function takes in a dataframe and a keyword,
    and performs forecasting using Facebook Prophet.
    """
    prophet_df = df[['date', keyword]].rename(columns={'date': 'ds', keyword: 'y'})    #Prepare the data for Prophet
    #Initialize and train the model
    model = Prophet()
    model.fit(prophet_df)

    #future dediction for 1year
    future = model.make_future_dataframe(periods=365)
    #Predict future values
    forecast = model.predict(future)

    # Plot the forecast
    model.plot(forecast)
    plt.title(f'Forecast: {keyword}')
    plt.xlabel('Date')
    plt.ylabel('Search Interest')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

##Step5 Run Forecast for Each Keyword
for label, df in trend_data.items():   # For each keyword in each topic pair, generate and plot the forecast
    for keyword in df.columns[1:]:
        forecast_keyword(df, keyword)

print("✅ All keyword pairs have been successfully analyzed and forecasted!")
print("📊 You generated Google Trends data, visualized historical trends, and predicted future interest using Prophet.")