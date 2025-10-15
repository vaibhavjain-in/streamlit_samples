import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.header('Matplotlib, Searborn and PLotly visualization in streamlit.')

# load the data
df = pd.read_csv('files/tips.csv')
st.dataframe(df.head())

st.markdown('---')
with st.container():
    st.write('1. Find number of Male and Female distribution (pie and bar)')
    value_counts = df['sex'].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Pie Chart')
        # draw pie chart
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct='%0.2f%%', labels=['Male', 'Female'])
        st.pyplot(fig)

    with col2:
        st.subheader('Bar Chart')
        # draw bar plot
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)

    # put this in expander
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)

# streamlit widgets and charts
data_types = df.dtypes
cat_cols = tuple(data_types[data_types == 'object'].index)

st.markdown('---')
with st.container():
    feature = st.selectbox('Select the feature you want to display bar and pie chart',
                           cat_cols
                           )
    value_counts = df[feature].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Pie Chart')
        # draw pie chart
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct='%0.2f%%', labels=value_counts.index)
        st.pyplot(fig)

    with col2:
        st.subheader('Bar Chart')
        # draw bar plot
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)

    # put this in expander
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)

## 2. Find distribution of Male and Female spent
st.markdown('---')
with st.container():
    st.write('2. Find distribution of Male and Female spent')
    # box, violin, kdeplot, histogram
    chart = ('box', 'violin', 'kdeplot', 'histogram')
    chart_selection = st.selectbox('Select the chart type', chart)
    fig, ax = plt.subplots()
    if chart_selection == 'box':
        sns.boxplot(x='sex', y='total_bill', data=df, ax=ax)
    elif chart_selection == 'violin':
        sns.violinplot(x='sex', y='total_bill', data=df, ax=ax)
    elif chart_selection == 'kdeplot':
        sns.kdeplot(x=df['total_bill'], hue=df['sex'], ax=ax, shade=True)
    else:
        sns.histplot(x='total_bill', hue='sex', data=df, ax=ax)

    st.pyplot(fig)

## 3. Find distribution of averge total_bill across each day by male and female
# bar, area, line
st.markdown('---')
st.write('3. Find distribution of averge total_bill across each day by male and female')

features_to_groupby = ['day', 'sex']
feature = ['total_bill']
select_cols = feature + features_to_groupby
avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
avg_total_bill = avg_total_bill.unstack()
# visual
fig, ax = plt.subplots()
avg_total_bill.plot(kind='bar', ax=ax)
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
st.pyplot(fig)

st.dataframe(avg_total_bill)

###
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        group_cols = st.multiselect('select the features', cat_cols, cat_cols[0])
        features_to_groupby = group_cols
        n_features = len(features_to_groupby)

    with c2:
        chart_type = st.selectbox('Select Chart type',
                                  ('bar', 'area', 'line'))

    with c3:
        stack_option = st.radio('Stacked', ('Yes', 'No'))
        if stack_option == 'Yes':
            stacked = True
        else:
            stacked = False

    feature = ['total_bill']
    select_cols = feature + features_to_groupby
    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
    if n_features > 1:
        for i in range(n_features - 1):
            avg_total_bill = avg_total_bill.unstack()

    avg_total_bill.fillna(0, inplace=True)

    # visual
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type, ax=ax, stacked=stacked)
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.set_ylabel('Avg Total Bill')
    st.pyplot(fig)

    with st.expander('click here to display values'):
        st.dataframe(avg_total_bill)

# 4. Find the relation between total_bill and tip on time (scatter plot)
st.markdown('---')
st.write('4. Find the relation between total_bill and tip on time')

fig, ax = plt.subplots()
hue_type = st.selectbox('Select the feature to hue', cat_cols)

sns.scatterplot(x='total_bill', y='tip', hue=hue_type, ax=ax, data=df)
st.pyplot(fig)

#Plotly
st.subheader('1. Draw histogram for total bill')

fig = px.histogram(data_frame=df,x='total_bill')
st.plotly_chart(fig, key='first')

st.subheader('2. Draw histogram for total bill and color by sex')
fig = px.histogram(data_frame=df,x='total_bill',color='sex')
st.plotly_chart(fig, key='second')

st.subheader('3. Draw histogram for total bill and color by (sex, smoker, day, time)')
select = st.selectbox('Select the category to color',
                      ('sex','smoker','day','time'))

fig = px.histogram(data_frame=df,x='total_bill',color=select)
st.plotly_chart(fig, key='third')

st.subheader("""
4. Draw Scatter plot between total_bill and tips and color by (('sex','day','smoker','time')')
""")
color_option = st.selectbox('Slect the category to color',
                            ('sex','smoker','day','time'))
fig = px.scatter(data_frame=df,x='total_bill',y='tip',color=color_option)
st.plotly_chart(fig, key='fourth')

st.subheader("5. Sunburst Chart on features ('day','smoker','time')")
path = st.multiselect('select the categorical features path',
                      ('day','smoker','time'))
fig = px.sunburst(data_frame=df,path=path)
st.plotly_chart(fig, key='fifth')
