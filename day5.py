# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:37:59 2022

@author: Z0190794
"""

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
    })
st.write(df)

st.write('Below is a DataFrame:',df,'Above is a dataframe.')

tempdata = np.random.randn(2,3)
tempdata
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['aa','b','c'])
c = alt.Chart(df2).mark_circle().encode(
     x='aa', y='b', size='c', color='c', tooltip=['aa', 'b', 'c'])
st.write(c)

df3 = pd.DataFrame(
    np.random.randn(4,5),
    columns=['1a','2b','3c','4d','5e']
    )
st.write(df3)