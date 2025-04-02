import streamlit as st
from snowflake.cortex import Complete
        
prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
response = Complete(model='claude-3-5-sonnet', prompt=prompt)
st.markdown(response)
