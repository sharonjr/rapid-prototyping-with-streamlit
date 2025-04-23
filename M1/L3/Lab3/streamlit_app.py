# Import Python libraries
import streamlit as st
import datetime
import numpy as np
import pandas as pd
import altair as alt
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(f"🏔️ Avalanche App")

# Get the current credentials
session = get_active_session()


## Load data
# Getting data into streamlit via sql to import table
df = session.sql("SELECT * FROM AVALANCHE.PUBLIC.CUSTOMER_REVIEWS")

# Here are different ways to display a DataFrame
# df
# st.dataframe(df)

# Figuring out the data type of a variable
# st.write(type(df)) # Snowpark DataFrame

## Let's convert to a Pandas DataFrame
# df = df.to_pandas()
# st.dataframe(df)


## Missing data
# Since our data is clean, let's introduce some missing values
# df_with_missing = df.where(np.random.choice([True, False], size=df.shape, p=[1 - 0.05, 0.05]))
# st.dataframe(df_with_missing)

# Let's see the missing values
# st.write(df.isna())
# st.write(df_with_missing.isna())
# st.dataFrame(df_with_missing.dropna())


# Data filtering
# df[df.PRODUCT == 'Alpine Skis']

# # Drop-down widget
# unique_products = sorted(df.PRODUCT.unique())
# selected_products = st.multiselect('Select product(s)', unique_products, unique_products)
# st.write('Selected products:', list(selected_products))
# df[df.PRODUCT.isin(selected_products)]


# # Calendar widget
# st.subheader('Dates')

# df['DATE'] = pd.to_datetime(df['DATE'])

# d = st.date_input(
#     "Select dates",
#     (df['DATE'].min().date(), df['DATE'].median().date() ),
#     df['DATE'].min().date(),
#     df['DATE'].max().date(),
# )

# # Check if both dates are specified
# if len(d)==2:
#     start_date = pd.to_datetime(d[0])
#     end_date = pd.to_datetime(d[1])

#     st.write('Selected dates:', start_date, end_date)
    
#     df_filtered = df[ (df['DATE'] >= start_date) & (df['DATE'] <= end_date) ]
#     df_filtered


#     ## Data visualization
#     st.subheader('Data visualization')
    
#     x_encoding = alt.X('DATE:T', axis=alt.Axis(format='%Y-%m-%d', labelAngle=90))
#     tooltip_encoding = ['DATE:T', 'SENTIMENT_SCORE:Q', 'PRODUCT:N']
    
#     sentiment_chart = alt.Chart(df_filtered).mark_bar(size=15).encode(
#         x=x_encoding,
#         y=alt.Y('SENTIMENT_SCORE:Q'),
#         color=alt.condition(
#             alt.datum.SENTIMENT_SCORE >= 0,
#             alt.value('#2ecc71'),  # green for positive
#             alt.value('#e74c3c')   # red for negative
#         ),
#         tooltip=tooltip_encoding
#     ).properties(
#         height=400
#     )
    
#     st.altair_chart(sentiment_chart, use_container_width=True)
