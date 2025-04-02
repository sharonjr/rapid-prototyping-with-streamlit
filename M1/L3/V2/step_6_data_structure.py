import streamlit as st
import time
import numpy as np

st.title("🏎️ Data Structure Performance Comparison")

def timer(func, *args, **kwargs):
    """Times the execution of a function and returns the time taken."""
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

# --- Dictionary vs. List Lookup ---
st.header("Dictionary vs. Python List *for* Lookup")

large_list = list(range(10000000))
large_dict = {i: i for i in range(10000000)}

dict_time = timer(lambda: 9999999 in large_dict)
list_time = timer(lambda: 9999999 in large_list)

st.write(f"Dictionary Lookup Time: `{dict_time:.5f}` seconds")
st.write(f"List Lookup Time: `{list_time:.5f}` seconds")

# --- NumPy Array vs. Python List for Numerical Computation ---
st.header("NumPy Array vs. Python List *for* Numerical Computation")

python_list = list(range(10000000))
numpy_array = np.arange(10000000)

numpy_array_time = timer(lambda: np.sum(numpy_array))
python_list_time = timer(lambda: sum(python_list))

st.write(f"NumPy Array Sum Time: `{numpy_array_time:.5f}` seconds")
st.write(f"Python List Sum Time: `{python_list_time:.5f}` seconds")