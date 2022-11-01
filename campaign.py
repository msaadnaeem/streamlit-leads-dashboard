import streamlit as st
import pandas as pd
import plotly.express as px

##Data read
df= pd.read_csv('leads_data.csv')
#Timestamp to Date
df['Timestamp']=pd.to_datetime(df['Timestamp']).dt.date
#Histogram
fig1=px.histogram(df, x='Timestamp', color='Type')
#Piechart
fig2=px.pie(df, values='ID', names='Brand')
leads = df.groupby(['Type']).count()
organicLeads=leads.iloc[0,0]
paidLeads=leads.iloc[1,0]
totalLeads=organicLeads+paidLeads

###Streamlit app
colLeft, colMid,colRight = st.columns((1,4,1))
with colMid:
    st.title('Campaign Dashboard')

##Metrics Cards
colLeft, colMid,colRight = st.columns((2,2,2))
with colLeft:
        st.metric(label='Toal Leads',value=totalLeads)
with colMid:
    st.metric(label='Organic Leads',value=organicLeads)
with colRight:
    st.metric(label='Paid Leads',value=paidLeads)

st.subheader('Daily Leads')
st.plotly_chart(fig1,use_container_width=True)

st.subheader('Brand Segments')
st.plotly_chart(fig2,use_container_width=True)

