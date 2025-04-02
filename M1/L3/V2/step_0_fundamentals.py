import streamlit as st  # Import the Streamlit library

st.set_page_config(layout="wide")  # Set the page layout to wide
st.title("🔤 Fundamentals")  # Set the title of the app

st.write("Hello, Streamlit!")  # Display text
st.write([1, 2, 3, 4])  # Display a list

st.sidebar.title("My Sidebar")  # Add a title to the sidebar
with st.sidebar:
    st.write("This is the sidebar.")  # Write to the sidebar

col1, col2 = st.columns(2)  # Create two columns

with col1:
    st.write("This is the first column.")  # Content for the first column
    st.header("A subheading")  # Add a subheading in the first column

with col2:
    st.write("This is the second column.")  # Content for the second column
