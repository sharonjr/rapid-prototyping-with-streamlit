import streamlit as st
import pandas as pd

st.title("🏔️ Avalanche Data Set")

df = pd.read_csv("data/customer_reviews.csv")
df
