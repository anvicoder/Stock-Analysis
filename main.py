import streamlit as st
import yfinance as fn

st.write(""" # Data Analysis of Stocks of Apple, Microsoft and Tesla """)

st.header("A Data Science Web App")
st.sidebar.header("Anviksha Patel \n Code with me...")
def get_ticker(name):
    company = fn.Ticker(name)
    return company

c1 = get_ticker("AAPL")
c2 = get_ticker("MSFT")
c3 = get_ticker("TSLA")

# fetching data for dataframe-
apple=fn.download("AAPL" , start="2021-11-11" , end="2023-10-11")
microsoft=fn.download("MSFT" , start="2021-11-11" , end="2023-10-11")
tesla=fn.download("TSLA" , start="2021-11-11" , end="2023-10-11")


#fetching historical data by valid periods 
data1 = c1.history(period="3mo")
data2 = c2.history(period="3mo")
data3 = c3.history(period="3mo ")

#Markdown"" ### Apple


# Center-align text using CSS style
st.write(""" ### Apple """)


# Detailed summary about apple company
st.write(c1.info['longBusinessSummary'])

#Dataframe
st.write(apple)

#Chart
st.line_chart(data1.values)

#Markdown
st.write(""" ### Microsoft """)

# Detailed summary about apple company
st.write(c2.info['longBusinessSummary'])

#Dataframe
st.write(microsoft)

#Chart
st.line_chart(data2.values)

#Markdown
st.write(""" ### Tesla """)

# Detailed summary about apple company
st.write(c3.info['longBusinessSummary'])

#Dataframe
st.write(tesla)

#Chart
st.line_chart(data3.values)