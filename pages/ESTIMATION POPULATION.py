import pandas as pd
import numpy as np
import plotly.graph_objs as go
from scipy.stats import chi2, norm
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
st.title("QUANTITATIVE RESEARCH")
st.header("POPULATION  ESTIMATION")
st.write("___")

# Load the CSV file
data = pd.read_csv('estimation.csv',)

# Extract the 'age' column
ages = data['age']

# Sample statistics
n = len(ages)
sample_mean = np.mean(ages)
sample_std = np.std(ages, ddof=1)  # Use ddof=1 for sample standard deviation

# Population size
N = 1000

# Confidence level
confidence_level = 0.95
alpha = 1 - confidence_level

# Critical values for chi-square distribution
df = n - 1
chi2_lower = chi2.ppf(alpha / 2, df)
chi2_upper = chi2.ppf(1 - alpha / 2, df)

# Confidence interval for population mean
sem = sample_std / np.sqrt(n)
margin_of_error_mean = sem * np.sqrt((N - n) / (N - 1))
lower_bound_mean = sample_mean - margin_of_error_mean
upper_bound_mean = sample_mean + margin_of_error_mean

# Confidence interval for population standard deviation
lower_bound_std = np.sqrt((df * sample_std ** 2) / chi2_upper)
upper_bound_std = np.sqrt((df * sample_std ** 2) / chi2_lower)

# Calculate standard error of the mean (SEM)
sem = sample_std / np.sqrt(n)

a1,a2,a3=st.columns(3)
b1,b2,b3=st.columns(3)
# Display outputs using Streamlit

a1.metric(label="Sample Mean (Age)", value=f"{sample_mean:.2f}")
a2.metric(label="Sample Standard Deviation (Age)", value=f"{sample_std:.2f}")
a3.metric(label="Population Size (N)", value=f"{N}")
b1.metric(label="95% CI for Population Mean (Age)", value=f"({lower_bound_mean:.2f}, {upper_bound_mean:.2f})")
b2.metric(label="95% CI for Population Standard Deviation (Age)", value=f"({lower_bound_std:.2f}, {upper_bound_std:.2f})")
b3.metric(label="Standard Error of the Mean (SEM):", value=f"({sem:.2f},")
 
 
# Calculate the critical z-values
z_critical = norm.ppf(1 - alpha/2)  # Two-tailed test

# Define the normal distribution parameters
x = np.linspace(sample_mean - 4*sem, sample_mean + 4*sem, 1000)
y = norm.pdf(x, sample_mean, sem)

# Create figure using Plotly
fig = go.Figure()

# Add the normal distribution curve
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution'))

# Calculate y values for shading under the curve
shade_x = np.linspace(sample_mean - z_critical*sem, sample_mean + z_critical*sem, 100)
shade_y = norm.pdf(shade_x, sample_mean, sem)

# Add shaded area for the confidence interval
fig.add_trace(go.Scatter(x=np.concatenate([shade_x, shade_x[::-1]]),
                         y=np.concatenate([shade_y, np.zeros_like(shade_x)]),
                         fill='toself', fillcolor='rgba(0,100,80,0.3)',
                         line=dict(color='rgba(255,255,255,0)'), name='95% CI',
                         hoverinfo="skip"))

# Add markers for sample mean and confidence interval boundaries
fig.add_trace(go.Scatter(x=[sample_mean], y=[norm.pdf(sample_mean, sample_mean, sem)], mode='markers',
                         marker=dict(color='red', size=10), name='Sample Mean'))
fig.add_trace(go.Scatter(x=[sample_mean - z_critical*sem, sample_mean + z_critical*sem],
                         y=[norm.pdf(sample_mean - z_critical*sem, sample_mean, sem), norm.pdf(sample_mean + z_critical*sem, sample_mean, sem)],
                         mode='markers', marker=dict(color='green', size=10), name='95% CI Bounds'))

# Update layout
fig.update_layout(title='Normal Distribution with 95% Confidence Interval',
                  xaxis_title='Age',
                  yaxis_title='Probability Density',
                  showlegend=True)

# Display Plotly figure using Streamlit
st.plotly_chart(fig)


