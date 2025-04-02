import streamlit as st
import aisuite as ai

st.title("🤖 Gen AI Example")

# Load API keys from st.secrets
openai_api_key = st.secrets.get("OPENAI_API_KEY")
anthropic_api_key = st.secrets.get("ANTHROPIC_API_KEY")

if not openai_api_key or not anthropic_api_key:
    st.error("Both OPENAI_API_KEY and ANTHROPIC_API_KEY are required. Please add them to secrets.")
else:
    client = ai.Client(api_keys={"openai": openai_api_key, "anthropic": anthropic_api_key})

    model = st.selectbox("Model:", ["openai:o3-mini", "anthropic:claude-3-5-sonnet-20240620"])
    prompt = st.text_input("Prompt:")

    if prompt:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(e)