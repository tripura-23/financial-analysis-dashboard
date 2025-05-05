import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App configuration
st.set_page_config(page_title="Financial Analysis Dashboard", layout="wide")
st.title("📊 End-to-End Financial Analysis Platform")

# File uploader
uploaded_file = st.file_uploader("Upload your stock CSV file", type=["csv"])

# If file is uploaded
if uploaded_file is not None:
    # Load CSV
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    df.sort_values('Date', inplace=True)
    df.set_index('Date', inplace=True)

    st.subheader("📁 Raw Data")
    st.dataframe(df.head())

    # Calculate indicators
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['Daily Return'] = df['Close'].pct_change()

    st.subheader("📈 Descriptive Statistics")
    st.write(df.describe())

    # Plot 1: Price & Moving Averages
    st.subheader("📉 Closing Price with Moving Averages")
    fig1, ax1 = plt.subplots(figsize=(12, 5))
    ax1.plot(df['Close'], label='Close Price', color='blue')
    ax1.plot(df['MA20'], label='20-Day MA', color='orange')
    ax1.plot(df['MA50'], label='50-Day MA', color='green')
    ax1.set_title('Stock Price with 20 & 50-Day Moving Averages')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)

    # Plot 2: Daily Return Distribution
    st.subheader("📊 Daily Return Distribution")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True, color='purple', ax=ax2)
    ax2.set_title('Daily Return Distribution')
    st.pyplot(fig2)

    # Plot 3: Correlation Heatmap
    st.subheader("🧮 Correlation Heatmap")
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax3)
    ax3.set_title('Feature Correlation Heatmap')
    st.pyplot(fig3)
else:
    st.info("Please upload a CSV file to begin.")
