import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")  
st.subheader("PYTHON QUERY OPERATIONS | FETCH DATA FROM DATASET BY ADVANCED QUERY")

theme_plotly = None 

#sidebar
st.sidebar.image("data/logo1.png")

# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    
# Load the Excel file into a DataFrame
file_path = 'python_query.xlsx'  
df = pd.read_excel(file_path)

with st.expander("🔷 **View Original Dataset | Excel file**"):
 st.dataframe(df,use_container_width=True)

# TASK 1: Display results using Streamlit metrics cards horizontally
# Query 1
with st.expander("**QUERY 1:** Select count **States** by Frequency"):
 state_count = df['State'].value_counts().reset_index()
 state_count.columns = ['State', 'Frequency']
 st.write("Count of States by Frequency:")
 st.dataframe(state_count,use_container_width=True)

# Bar graph for Query 2
with st.expander("**QUERY 2:** select count **State** by frequency and print in dataframe and show simple bar graph with grids and legend"):
 fig3 = px.bar(state_count, x='State', y='Frequency', labels={'x': 'State', 'y': 'Frequency'}, title='Frequency of States')
 fig3.update_layout(showlegend=True)
 fig3.update_xaxes(showgrid=True)
 fig3.update_yaxes(showgrid=True)
 st.plotly_chart(fig3,use_container_width=True)

# Query 3
with st.expander("**QUERY 3:** Select count **BusinessType** by frequency"):
 business_type_count = df['BusinessType'].value_counts().reset_index()
 business_type_count.columns = ['BusinessType', 'Frequency']
 st.write("Count of Business Types by Frequency:")
 st.dataframe(business_type_count,use_container_width=True)

# Bar graph for Query 4
with st.expander("**QUERY 4:** select count **BusinessType**  by frequency and print in dataframe and show simple bar graph with grids and legend"):
 fig4 = px.bar(business_type_count, x='BusinessType', y='Frequency', labels={'x': 'BusinessType', 'y': 'Frequency'}, title='Frequency of Business Types')
 fig4.update_layout(showlegend=True)
 fig4.update_xaxes(showgrid=True)
 fig4.update_yaxes(showgrid=True)
 st.plotly_chart(fig4,use_container_width=True)

# Query 5
with st.expander("**QUERY 5:** select minimal **Investment** and minimal **Rating** where **State** is Mwanza and date is range from 2-jan-21 to 16-jan-21"):
 query_5 = df[(df['State'] == 'Mwanza') & (df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16')][['Investment', 'Rating']].agg('min')
 st.success("Minimum **Investment** and **Rating** where **State** is **Mwanza** and date is in the specified range:")
 st.dataframe(query_5)


# Query 6
with st.expander("**QUERY 6:** select count **Location** where **Location** ='Dodoma'"):
 count_location = df[df['State'] == "Dodoma"]['Location'].count()
 st.info(f"## {count_location}")

# Query 7
with st.expander("**QUERY 7:** > select count  **Location** and **Region** where **Location** ='Dodoma' and **Region**='East'"):
 count_location_region = df[(df['State'] == "Dodoma") & (df['Region'] == "East")]['Location'].count()
 st.info(f"## {count_location_region:,.3f}")

# Query 8
with st.expander("**QUERY 8:** select count **Location** and **Region** where **Location** ='Dodoma' and **Region**='East' and **Investment** is greater than 300000"):
 count_location_region_investment = df[(df['State'] == "Dodoma") & (df['Region'] == "East") & (df['Investment'] > 300000)]['Location'].count()
 st.info(f"## {count_location_region_investment:,.3f}")

# Query 9
with st.expander("**QUERY 9:** select average mean of **investment** where **State**='Dodoma' and **Location** is not  'Urban'"):
 avg_investment_dodoma_not_urban = df[(df['State'] == "Dodoma") & (df['Location'] != "Urban")]['Investment'].mean()
 st.info(f"## {avg_investment_dodoma_not_urban:,.3f} ")


# Query 10- Sum of investments in the date range at Dodoma
with st.expander("**QUERY 10:** select summation of **investment** where **Expiry** is a date range from 2-jan-21 to 16-jan-21 and region is Dodoma"):
 sum_investment_date_range_dodoma = df[(df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16') & (df['State'] == 'Dodoma')]['Investment'].sum()
 st.info(f"## {sum_investment_date_range_dodoma:,.3f}")


# Query 11
with st.expander("**QUERY 11:** select Median of **Investment**  and **Rating** where **State** is Mwanza, **Location** is Urban and **Investment** is greater than 400,000"):
 query_1 = df[(df['State'] == 'Mwanza') & (df['Location'] == 'Urban') & (df['Investment'] > 400000)][['Investment', 'Rating']].median()
 st.success("Median of **Investment** and **Rating** where **State** is Mwanza, **Location** is Urban, and **Investment** is greater than 400,000 USD:")
 st.dataframe(query_1)

# Query 12
with st.expander("**QUERY 12:** select median of **Investment**  and **Rating** where **State** is Mwanza **Location** is Urban and **Investment** is greater than 400,000 and **Expiry** is a date range from 2-jan-21 to 16-jan-21"):
 query_2 = df[(df['State'] == 'Mwanza') & (df['Location'] == 'Urban') & (df['Investment'] > 400000) & (df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16')][['Investment', 'Rating']].median()
 st.success("Median of Investment and Rating where State is Mwanza, Location is Urban, Investment is greater than 400000, and Expiry is in the specified date range:")
 st.dataframe(query_2)


#Display tables using st.dataframe()

st.success("SELECT QUERY RESULTS IN TABULAR")

# Query 12
with st.expander('**QUERY 13:** Select all from **Location** where **Location** ="Dodoma"'):
 st.dataframe(df[df['State'] == "Dodoma"],use_container_width=True)

# Query 14
with st.expander('**QUERY 14:** Select all from **Location** and **Region** where **Location** ="Dodoma" and **Region**="East"'):
 st.dataframe(df[(df['State'] == "Dodoma") & (df['Region'] == "East")],use_container_width=True)

# Query 15
with st.expander('**QUERY 15:** Select all from **Location** and **Region** where **Location** ="Dodoma" and **Region**="East" and **Investment** is greater than 300,000'):
 st.dataframe(df[(df['State'] == "Dodoma") & (df['Region'] == "East") & (df['Investment'] > 300000)],use_container_width=True)

# Query 16
with st.expander('**QUERY 16:** Select all  **investment** where **State**="Dodoma" and **Location** is not "Urban"'):
 st.dataframe(df.loc[(df['State'] == "Dodoma") & (df['Location'] != "Urban"), 'Investment'],use_container_width=True)

# Query 17
with st.expander('**QUERY 17:** select at least 5 most frequent **Investment** where **Expiry** is a date range from 2-jan-21 to 16-jan-21'):
 freq_investment_date_range = df[(df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16')]['Investment'].value_counts().nlargest(5).reset_index()
 st.dataframe(freq_investment_date_range.rename(columns={'index': 'Investment', 'Investment': 'Count'}))

# Query 18
with st.expander('**QUERY 18:** select all **investments** where **Expiry** is a date range from 2-jan-21 to 16-jan-21 and region is **Dodoma**'):
 st.dataframe(df.loc[(df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16') & (df['State'] == 'Dodoma'), 'Investment'],use_container_width=True)

#Query 19
with st.expander("**QUERY 19:** select **State**, **Region**, **Location** and  **BusinessType**  where **Region** is 'East'and **investment** greater than 2219900 and **BusinessType** is not  'Other' and **Construction** is Frame or FireResist and **State** is Dar es Salaam or Dodoma"):
# Applying the specified conditions
 query_result = df[
    (df['Region'] == 'East') &
    (df['Investment'] > 2219900) &
    (df['BusinessType'] != 'Other') &
    (df['Construction'].isin(['Frame', 'Fire Resist'])) &
    (df['State'].isin(['Dar es Salaam', 'Dodoma']))
 ][['State', 'Region', 'Location', 'BusinessType']]
 st.dataframe(query_result,use_container_width=True)
