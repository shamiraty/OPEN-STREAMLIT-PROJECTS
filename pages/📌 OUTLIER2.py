import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm, zscore
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
import plotly.express as px

# Set page configuration for wide layout
st.set_page_config(layout="wide")

# Custom CSS for sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #103F7A;
    }
    [data-testid="stSidebar"] * {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with header
with st.sidebar:
    st.header("DASHBOARD")

# Main title and description
st.title('DATA SCIENCE')
st.title("Outlier Detection Techniques")
st.write("""
This app detects anomalies in the 'age' column of a dataset using multiple outlier detection techniques:
- **Isolation Forest | Contamination**
- **Local Outlier Factor (LOF)**
- **Normal Distributions and Z-scores (X~N(0:1))**
- **Quartiles**
- **Percentile-Based Method**
- **Outliers Treatment Techniques [Winsorization]**       
""")

### Normal Distribution & Z-Scores Section
st.success("## 1. Normal Distribution & Z-scores")

# Load dataset
df = pd.read_csv('dataset.csv')

# Get min and max age for plotting
max_age = df['age'].max()
min_age = df['age'].min()

# Create figure for PDF
fig_pdf = go.Figure()

# Plot Normal distribution curve
x_values = np.linspace(min_age, max_age, 100)
normal_pdf = norm.pdf(x_values, df['age'].mean(), df['age'].std())
fig_pdf.add_trace(go.Scatter(x=x_values, y=normal_pdf, mode='lines', name='Normal Distribution', line=dict(color='blue')))

# Highlight outliers using z-scores
z_scores = zscore(df['age'])
outliers = df[(z_scores < -3) | (z_scores > 3)]
fig_pdf.add_trace(go.Scatter(x=outliers['age'], y=[0]*len(outliers), mode='markers', name='Outliers', marker=dict(color='red', size=10)))

# Update PDF figure layout
fig_pdf.update_layout(title='Probability Density Function (PDF) of Age', xaxis_title='Age', yaxis_title='Density', showlegend=True)
st.plotly_chart(fig_pdf, use_container_width=True)

# Create layout for Box Plot and Outlier Values
a, b = st.columns([3, 1])

# Box Plot of Age
a.subheader('Box Plot of Age')
fig_box = go.Figure()
fig_box.add_trace(go.Box(y=df['age'], boxpoints='outliers', marker_color='blue', name='Age Distribution'))

# Add quartile annotations
quartiles = np.percentile(df['age'], [25, 50, 75])
quartile_text = [f"Q{i}: {quartile:.2f}" for i, quartile in enumerate(quartiles, start=1)]
fig_box.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(color='white', size=0), name=', '.join(quartile_text)))

a.plotly_chart(fig_box, use_container_width=True)

# Display outlier values
b.subheader('Outlier Values')
b.dataframe(outliers[['age']], use_container_width=True)

### Isolation Forest Section
st.success("## 2. Isolation Forest")

# Fit the Isolation Forest model
iso_forest = IsolationForest(contamination=0.01, random_state=42)
iso_forest.fit(df[['age']])
df['anomaly'] = iso_forest.predict(df[['age']])

# Identify outliers
iso_outliers = df[df['anomaly'] == -1]

# Display the outliers detected by Isolation Forest
st.write("### Detected Outliers (Isolation Forest)")
st.dataframe(iso_outliers, use_container_width=True)

# Plotting graphs for Isolation Forest
c1, c2 = st.columns(2)

with c1:
    # Scatter Plot for Isolation Forest
    st.write("### Scatter Plot of Age with Outliers Highlighted (Isolation Forest)")
    scatter_fig = px.scatter(df, x=df.index, y='age', color='anomaly',
                             color_discrete_map={1: 'blue', -1: 'red'},
                             labels={'color': 'Anomaly'})
    st.plotly_chart(scatter_fig, use_container_width=True)

with c2:
    # Box Plot for Isolation Forest
    st.write("### Box Plot of Age with Outliers Highlighted (Isolation Forest)")
    box_fig = px.box(df, x='anomaly', y='age', color='anomaly',
                     color_discrete_map={1: 'blue', -1: 'red'},
                     labels={'anomaly': 'Anomaly', 'age': 'Age'})
    st.plotly_chart(box_fig, use_container_width=True)

### Local Outlier Factor (LOF) Section
st.success("## 3. Local Outlier Factor (LOF)")

# Fit the Local Outlier Factor (LOF) model
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.01)
df['lof_anomaly'] = lof.fit_predict(df[['age']])
lof_outliers = df[df['lof_anomaly'] == -1]

# Plotting graphs for LOF
d1, d2 = st.columns(2)

with d1:
    # Scatter Plot for LOF
    st.write("### Scatter Plot of Age with Outliers Highlighted (LOF)")
    scatter_fig_lof = px.scatter(df, x=df.index, y='age', color='lof_anomaly',
                                 color_discrete_map={1: 'blue', -1: 'red'},
                                 labels={'color': 'Anomaly'})
    st.plotly_chart(scatter_fig_lof, use_container_width=True)

with d2:
    # Box Plot for LOF
    st.write("### Box Plot of Age with Outliers Highlighted (LOF)")
    box_fig_lof = px.box(df, x='lof_anomaly', y='age', color='lof_anomaly',
                         color_discrete_map={1: 'blue', -1: 'red'},
                         labels={'lof_anomaly': 'Anomaly', 'age': 'Age'})
    st.plotly_chart(box_fig_lof, use_container_width=True)

# Display outliers detected by LOF
st.write("### Detected Outliers (LOF)")
st.dataframe(lof_outliers, use_container_width=True)



### Percentile-Based Method Section
st.success("## 5. Percentile-Based Method")

# Define thresholds for top and bottom percentiles
top_percentile = 95
bottom_percentile = 5

# Calculate percentile values
top_threshold = np.percentile(df['age'], top_percentile)
bottom_threshold = np.percentile(df['age'], bottom_percentile)

# Identify outliers
percentile_outliers_top = df[df['age'] > top_threshold]
percentile_outliers_bottom = df[df['age'] < bottom_threshold]

# Print outliers
st.write("### Top Percentile Outliers")
st.dataframe(percentile_outliers_top,use_container_width=True)

st.write("### Bottom Percentile Outliers")
st.dataframe(percentile_outliers_bottom,use_container_width=True)


st.success("## Outliers Treatment Techniques")
st.success("> Winsorization, or winsorizing, is the process of transforming the data by limiting the extreme values, that is, the outliers, to a certain arbitrary value, closer to the mean of the distribution. Winsorizing is different from trimming because the extreme values are not removed, but are instead replaced by other values. A typical strategy involves setting outliers to a specified percentile.")
# Define the percentile values for Winsorization
winsor_percentile = 5  # Set to 5th and 95th percentile for lower and upper bounds

# Calculate Winsorization bounds
lower_bound = np.percentile(df['age'], winsor_percentile)
upper_bound = np.percentile(df['age'], 100 - winsor_percentile)

# Winsorization
df['age_winsorized'] = df['age'].clip(lower=lower_bound, upper=upper_bound)

# Concatenate original and winsorized data along columns axis
concatenated_df = pd.concat([df[['age']], df[['age_winsorized']]], axis=1)
concatenated_df.columns = ['Original Age', 'Winsorized Age']

# Display concatenated data
st.dataframe(concatenated_df,use_container_width=True)
