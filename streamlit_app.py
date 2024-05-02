import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

# Title of the webpage
st.title('Streamlit Example App')

# Markdown can be used to add description text
st.markdown("""
This is a simple Streamlit app for demonstrating basic functionality including:
- Input fields
- Dynamic computation
- Graphing capabilities
""")

# User input: number of data points
num_data_points = st.slider('Select number of data points', min_value=10, max_value=1000, value=500)

# Generate random data
data = np.random.randn(num_data_points)
df = pd.DataFrame(data, columns=['Random numbers'])

# Display the data as a table
st.write("Data Preview:")
st.write(df.head())

# Plotting the data
fig, ax = plt.subplots()
ax.hist(data, bins=20, alpha=0.5, color='blue')
ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Random Numbers')
st.pyplot(fig)

# Optional: Display the raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(df)

# You can also use other libraries like seaborn for more complex visualizations
# import seaborn as sns
# sns.histplot(data)
# st.pyplot()

