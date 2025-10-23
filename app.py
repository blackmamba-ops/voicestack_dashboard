# app.py
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from textblob import TextBlob

st.set_page_config(page_title="Voicestack Call Analytics", layout="wide")

# --- Load data ---
@st.cache_data
def load_data():
    df = pd.read_excel("/home/basil-k-aji/Workspace/Carestack_Assignment/dataset/Assignment Dataset.xlsx")
    df['Call Time'] = pd.to_datetime(df['Call Time'])
    return df

df = load_data()

st.title("📞 Voicestack Call Analytics Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("Filters")
start_date = st.sidebar.date_input("Start Date", df["Call Time"].min())
end_date = st.sidebar.date_input("End Date", df["Call Time"].max())
direction = st.sidebar.multiselect("Call Direction", df["Call Direction"].unique())
status = st.sidebar.multiselect("Call Status", df["Call Status"].unique())

mask = (
    (df["Call Time"].dt.date >= start_date)
    & (df["Call Time"].dt.date <= end_date)
)
if direction:
    mask &= df["Call Direction"].isin(direction)
if status:
    mask &= df["Call Status"].isin(status)

filtered_df = df[mask]

st.write(f"### Showing {len(filtered_df)} calls from {start_date} to {end_date}")

# --- KPIs ---
total_calls = len(filtered_df)
answered = (filtered_df["Call Status"] == "Answered").sum()
missed = (filtered_df["Call Status"] == "Missed").sum()
avg_duration = filtered_df["Conversation Duration"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("📞 Total Calls", total_calls)
col2.metric("✅ Answered", answered)
col3.metric("⏱️ Avg. Duration (s)", f"{avg_duration:.1f}")

# --- Sentiment Analysis ---
if "transcript" in filtered_df.columns:
    filtered_df["Sentiment"] = filtered_df["transcript"].apply(
        lambda x: TextBlob(str(x)).sentiment.polarity
    )

# --- Placeholder: Call Categorization ---
if "transcript" in filtered_df.columns:
    def categorize_call(text):
        text = str(text).lower()
        if "book" in text or "appointment" in text:
            return "Booking"
        elif "cancel" in text or "reschedule" in text:
            return "Cancellation"
        elif "bill" in text or "payment" in text:
            return "Billing"
        elif "insurance" in text:
            return "Insurance"
        elif "tooth" in text or "pain" in text or "treatment" in text:
            return "Clinical"
        else:
            return "Other"

    filtered_df["Call Category"] = filtered_df["transcript"].apply(categorize_call)

# --- Additional KPIs ---
if "Call Category" in filtered_df.columns:
    total_bookings = (filtered_df["Call Category"] == "Booking").sum()
    booking_rate = total_bookings / total_calls * 100 if total_calls > 0 else 0
    cancellations = (filtered_df["Call Category"] == "Cancellation").sum()

    col4, col5 = st.columns(2)
    col4.metric("📅 Booking Rate", f"{booking_rate:.1f}%")
    col5.metric("❌ Cancellations", cancellations)

# --- Call Volume Over Time ---
calls_over_time = (
    filtered_df.groupby(filtered_df["Call Time"].dt.date)
    .size()
    .reset_index(name="Count")
)
fig1 = px.line(calls_over_time, x="Call Time", y="Count", title="📅 Call Volume Over Time")
st.plotly_chart(fig1, use_container_width=True)

# --- Direction Split ---
fig2 = px.pie(filtered_df, names="Call Direction", title="📊 Call Direction Split")
st.plotly_chart(fig2, use_container_width=True)

# --- Status Split ---
status_counts = filtered_df["Call Status"].value_counts().reset_index()
status_counts.columns = ["Status", "Count"]

fig3 = px.bar(
    status_counts,
    x="Status",
    y="Count",
    title="📈 Call Status Distribution",
)
st.plotly_chart(fig3, use_container_width=True)

# --- Call Category Distribution ---
if "Call Category" in filtered_df.columns:
    category_counts = filtered_df["Call Category"].value_counts().reset_index()
    category_counts.columns = ["Category", "Count"]

    fig4 = px.bar(
        category_counts,
        x="Category",
        y="Count",
        title="📊 Call Category Distribution",
    )
    st.plotly_chart(fig4, use_container_width=True)

# --- Sentiment Distribution ---
if "Sentiment" in filtered_df.columns:
    fig5 = px.histogram(
        filtered_df,
        x="Sentiment",
        nbins=20,
        title="😊 Call Sentiment Distribution",
    )
    st.plotly_chart(fig5, use_container_width=True)

# --- Sentiment by Call Category ---
if "Sentiment" in filtered_df.columns and "Call Category" in filtered_df.columns:
    fig6 = px.box(
        filtered_df,
        x="Call Category",
        y="Sentiment",
        title="😊 Sentiment by Call Category",
    )
    st.plotly_chart(fig6, use_container_width=True)
