import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame(np.random.randn(10, 20),
  columns = ('col %d' % i
    for i in range(20)))
dataframe

dataframe = pd.DataFrame(np.random.randn(10, 5),
  columns = ('col %d' % i
    for i in range(5)))
dataframe
st.write('This is a line_chart.')
st.line_chart(dataframe)