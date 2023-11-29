import pandas as pd
import numpy as np
from scipy import stats
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objects as go
fig = go.Figure()
 
st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")

st.header("HYPOTHESIS  TESTING UNDER T-STUDENT DISTRIBUTION CURVE, TWO TAILED TEST")  
theme_plotly = None 

st.subheader("𝑡=(𝑋 ̅−𝜇)/(𝑆⁄√𝑛)~𝑡(𝑛−1)")
# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#Logo
st.sidebar.image("logo1.png")

#read dataset
df=pd.read_excel("hypothesis.xlsx")

#drop unnecessary field
df.drop(columns=["Date"],axis=1,inplace=True)

# Steps for hypothesis testing
# 1. Formulate null and alternative hypothesis
st.info("**Null hypothesis: The average Revenue of Group A and Group B are the same.**")
st.info("**Alternative hypothesis: The average Revenue  of Group A and Group B are different.**")

# 2. Determine confidence level
confidence_level = 0.95  

# 3. Determine test statistic
# Assuming the sample size is small (<30), we'll use a t-test for independent samples.
t_stat, p_value = stats.ttest_ind(df['GroupA'], df['GroupB'])

# Basic statistics from the DataFrame
sample_mean = df.mean()
sample_std = df.std()
sample_size = df.shape[0]


import sys
if sample_size >=30 :
    st.error(f" ERROR: T student is for sample size less than 30. unable to solve for **{sample_size}** sample size")
    sys.exit()


# 4. Normal distribution and critical value
alpha = 1 - confidence_level
critical_value = stats.t.ppf(1 - alpha / 2, df=sample_size - 1)  # Two-tailed test

# Generate x values for the normal distribution curve
x = np.linspace(-4, 4, 1000)
# Generate the normal distribution curve
y = stats.t.pdf(x, df=sample_size - 1)

# 5. Compute actual value
# The t-statistic is our computed value

# 6. Plotting
# Decision-making based on the computed t-statistic and critical value
if abs(t_stat) > critical_value:
    st.success("**✔ REJECT NULL HYPOTHESIS:** The average Revenue  of Group A and Group B are not the same")
else:
    st.success("#### **⚠ FAIL TO REJECT NULL HYPOTHESIS:** The average Revenue of Group A and Group B are the same")

# Plotting the probability density curve
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='gray'), name='Probability Density'))

# Adding vertical lines for critical value, t-statistic, and center
fig.add_shape(type="line", x0=critical_value, y0=0, x1=critical_value, y1=max(y),
              line=dict(color='red', width=2, dash='dash'), name=f'Critical Value: {critical_value:.2f}')
fig.add_shape(type="line", x0=t_stat, y0=0, x1=t_stat, y1=max(y),
              line=dict(color='green', width=2), name=f'T-statistic: {t_stat:.2f}')
fig.add_shape(type="line", x0=0, y0=0, x1=0, y1=max(y),
              line=dict(color='blue', width=2), name='Center: 0')

# Filling the rejection region
x_fill = np.linspace(critical_value, max(x), 100)
y_fill = stats.t.pdf(x_fill, df=4)
fig.add_trace(go.Scatter(x=np.concatenate([x_fill, x_fill[::-1]]), 
                         y=np.concatenate([y_fill, [0] * len(y_fill)]),
                         fill='tozeroy', fillcolor='wheat', mode='none', 
                         name='Rejection Region'))

# Adding values to the legend
fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers',
                         marker=dict(color='red', size=0),
                         name=f'Critical Value: {critical_value:.2f}'))
fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers',
                         marker=dict(color='green', size=0),
                         name=f'T-statistic: {t_stat:.2f}'))

# Layout settings
fig.update_layout(
    title='T DISTRIBUTION',
    xaxis_title='T-STATISTIC',
    yaxis_title='PROBABILITY DENSITY',
    showlegend=True,
    legend=dict(x=0, y=1),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    width=900,
    height=600
)

 
col1,col2=st.columns([1,2])

with col1:
 st.write("SAMPLE MEAN GROUP A AND B")
 st.dataframe(sample_mean,use_container_width=True)
 st.write("SAMPLE STANDARD DEV GROUP A AND B")
 st.dataframe(sample_std,use_container_width=True)

with col2:
 a1,a2,a3=st.columns(3)
 a1.metric("SAMPLE SIZE",f"{sample_size:,.0f}")
 a2.metric("COMPUTED VALUE",f"{t_stat:,.3f}")
 a3.metric("CRITICAL VALUE",f"{critical_value:,.3f}")
 style_metric_cards(background_color="#FFFFFF",border_left_color="red",border_color="blue",box_shadow="grey")
 st.plotly_chart(fig,use_container_width=True)

