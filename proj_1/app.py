import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Covid-19 EDA and visualization")

st.markdown(""" A web app to visualize and analyze the covid-19 data from india 
* **Libraries Used:** Streamlit, Pandas, Plotly
* **Author:** Dharavath Ramdas
""")

## inserting Image
st.image('https://preparecenter.org/wp-content/uploads/2020/05/IFRC-yellow-COVID-banner-1024x448.png', caption="Image by sachin")

## read csv data
df = pd.read_csv(r"https://raw.githubusercontent.com/imdevskp/covid-19-india-data/master/complete.csv")
# displaying data and its shape
st.write("Covid - 199 dataset",df)
st.write("Shape of data",df.shape)

# header of sidebar
st.sidebar.header("User Input")
# creating selectbox for graph and plots
graphs = st.sidebar.selectbox("Graphs and Plots",("Bar Graph","Scatter Plot","HeatMap","pie Chart"))
# sorting the columns
index = sorted(df.columns.unique())
# Setting default value for x,y and color
default_index_x = index.index("Name of State / UT")
default_index_y = index.index("Total Confirmed cases")
default_index_col = index.index('Death')

# Creating selectbox for x, y and color label and setting default value
x_label = st.sidebar.selectbox("X label Parameter", index, index=default_index_x)
y_label = st.sidebar.selectbox("Y label Parameter", index, index=default_index_y)
col = st.sidebar.selectbox("Color", index, index=default_index_col)

st.markdown('''
## **Visualization**
''')
# function to plot graphs
def visualize_plotly(graph):
    if graph == "Bar Graph":
        st.write(graph)
        fig = px.bar(df, x=x_label, y=y_label, color=col)

    elif graph == "Scatter Plot":
        st.write(graph)
        fig = px.scatter(df, x=x_label, y=y_label, color=col)

    elif graph == "HeatMap":
        st.write(graph)
        fig = px.density_heatmap(df, x=x_label, y=y_label, nbinsx=20, nbinsy=20)

    else:
        st.write(graph)
        fig = px.pie(df, values=x_label, names=df[y_label])

    return fig

figure = visualize_plotly(graphs)

st.plotly_chart(figure)

st.markdown('''
## **Report**
''')
# Creating buttons to display reports
if st.button("Highest Cases"):
    st.header("Highest Cases in a State/UT")
    highest_cases = df[df['Total Confirmed cases'] == max(df['Total Confirmed cases'])]
    st.write(highest_cases)

if st.button("Lowest Cases"):
    st.header("Lowest Cases in a State/UT")
    lowest_cases = df[df['Total Confirmed cases'] == min(df['Total Confirmed cases'])]
    st.write(lowest_cases)

if st.button("Highest New Cases"):
    st.header("Highest New Cases in a State/UT")
    high_active_cases = df[df['New cases'] == max(df['New cases'])]
    st.write(high_active_cases)

if st.button("Lowest Active Cases"):
    st.header("Lowest Active Cases in a State/UT")
    low_active_cases = df[df['New cases'] == min(df['Total Cases'])]
    st.write(low_active_cases)

if st.button("Highest Death"):
    st.header("Highest Death in a State/UT")
    high_death = df[df['Death'] == max(df['Death'])]
    st.write(high_death)

if st.button("Lowest Death Ratio (%)"):
    st.header("Lowest Death Ratio (%) in a State/UT")
    low_death = df[df['Death'] == min(df['Death'])]
    st.write(low_death)