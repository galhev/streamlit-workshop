import plotly.express as px
import streamlit as st
from datasets import load_dataset
import pandas as pd


dataset = load_dataset('mstz/heart_failure')
df = pd.DataFrame.from_dict(dataset['train'])
df['gender'] = df['is_male'].replace({False:'Female', True:'Male'})

hist_fig = px.histogram(df, x="age", color="has_high_blood_pressure")
barplot_fig = px.histogram(df, x="gender",
             color='has_high_blood_pressure', barmode='group',
              title='Histogram of blood pressure among people with cardiovascular disease',
                   labels={'has_high_blood_pressure':'has high blood pressure'})
boxplot_fig = px.box(df, x="is_dead", y="heart_ejection_fraction", color="gender")
boxplot_fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default


st.title('Dropdown Example')
option = st.selectbox(
   "Which plot do you want to present?",
   ("histogram", "boxplot", "bar plot"),
   index=None,
   placeholder="Select plot...",
)

if option == "histogram":
    st.plotly_chart(hist_fig, theme="streamlit", use_container_width=True)
if option == "bar plot":
    st.plotly_chart(barplot_fig, theme=None, use_container_width=True)
if option == "boxplot":
    st.plotly_chart(boxplot_fig, theme=None, use_container_width=True)