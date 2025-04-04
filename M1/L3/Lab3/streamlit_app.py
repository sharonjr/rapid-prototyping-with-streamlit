# Iteration 1
import streamlit as st
from snowflake.cortex import Complete
        
prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
response = Complete(model='claude-3-5-sonnet', prompt=prompt)
st.markdown(response)


# # Iteration 2
# import streamlit as st
# from snowflake.cortex import Complete
        
# st.title('❄️ LLM Demo')
        
# prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
# if st.button("Submit", type='primary'):
#     response = Complete(model='claude-3-5-sonnet', prompt=prompt)
#     st.markdown(response)

    
# # Iteration 3
# import streamlit as st
# from snowflake.cortex import Complete

# st.title('❄️ LLM Demo')

# with st.sidebar:
#     models = ['claude-3-5-sonnet', 'mistral-7b', 'gemma-7b', 'llama3-8b']
#     model = st.selectbox('Select a model', models)

# prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
# if st.button("Submit", type='primary'):
#     response = Complete(model=model, prompt=prompt)
#     st.markdown(response)
#     st.write(':orange[Selected model:]', model)
