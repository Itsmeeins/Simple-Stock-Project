import yfinance as yf
import streamlit as st


st.write("""
# Simple Stock Price App 📈

Before you go . I would like to express my gratitude to **Chanin Nantasenamat (อ.เอิร์ล)**, also known as **Data Professor**, for assisting me in launching this straightforward project. ❤️❤️❤️


Check out Data professor at https://www.youtube.com/dataprofessor


#### This web app show the Open , Close , Volume , All time high & All time low of Stock you looking for
""")



# Get the ticker symbol from the user
ticker_symbol = st.text_input("Enter the ticker symbol:")

# Query the data for the ticker symbol
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2022-12-20')

chart_type = st.selectbox("Select chart type:", ("Open", "Close", "Volume" ,"All time high", "All time low"))

if chart_type == "Open":
    st.line_chart(ticker_df.Open)
elif chart_type == "Close":
    st.line_chart(ticker_df.Close)
elif chart_type == "Volume":
    st.line_chart(ticker_df.Volume)
elif chart_type == "All time high":
    st.line_chart(ticker_df.High)
elif chart_type == "All time low":
    st.line_chart(ticker_df.Low)