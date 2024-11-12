import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, norm
import plotly.graph_objects as go
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
st.set_page_config(layout="wide")

def load_data():
    return pd.read_csv('dataset.csv')

st.sidebar.image("logo2.png",caption="EmployeeEcho Insights")
theme_plotly = None 

# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def calculate_age_intervals(max_age):
    intervals = np.arange(0, max_age + 11, 10)  # Adjusted to include maximum age
    labels = [f'{i}-{i+10}' for i in range(0, max_age + 1, 10)]  # Adjusted to include maximum age
    return intervals, labels

def calculate_grouped_statistics(freq_table):
    # Convert 'Age Interval' to numerical midpoints
    def get_midpoint(interval):
        start, end = map(int, interval.split('-'))
        return (start + end) / 2
    
    # Apply midpoint function and ensure numerical type
    freq_table['Midpoint'] = freq_table['Age Interval'].apply(get_midpoint).astype(float)

    # Calculate cumulative frequency
    freq_table['Cumulative Frequency'] = freq_table['Frequency'].cumsum()

    # Calculate mean
    mean_grouped = (freq_table['Midpoint'] * freq_table['Frequency']).sum() / freq_table['Frequency'].sum()

    # Calculate mode class
    mode_class = freq_table.loc[freq_table['Frequency'].idxmax()]['Age Interval']
    mode_class_start, mode_class_end = map(int, mode_class.split('-'))
    mode_freq = freq_table.loc[freq_table['Age Interval'] == mode_class, 'Frequency'].values[0]
    cumulative_freq_before = freq_table['Frequency'].cumsum().loc[freq_table['Age Interval'] == mode_class].values[0] - mode_freq
    mode = mode_class_start + ((mode_freq - cumulative_freq_before) / (2 * mode_freq)) * (mode_class_end - mode_class_start)

    # Calculate median
    total_freq = freq_table['Frequency'].sum()
    cumulative_freq = freq_table['Cumulative Frequency']
    median_class = freq_table.loc[cumulative_freq >= (total_freq / 2)].iloc[0]['Age Interval']
    median_class_start, median_class_end = map(int, median_class.split('-'))
    median_freq = freq_table.loc[freq_table['Age Interval'] == median_class, 'Frequency'].values[0]
    cumulative_freq_before = cumulative_freq[freq_table['Age Interval'] == median_class].values[0] - median_freq
    median = median_class_start + ((total_freq / 2 - cumulative_freq_before) / median_freq) * (median_class_end - median_class_start)

    # Calculate variance
    variance = ((freq_table['Midpoint'] - mean_grouped)**2 * freq_table['Frequency']).sum() / freq_table['Frequency'].sum()
    std_dev = np.sqrt(variance)

    # Calculate skewness
    skewness_grouped = skew(freq_table['Midpoint'].repeat(freq_table['Frequency']))

    # Calculate kurtosis
    kurtosis_value = kurtosis(freq_table['Midpoint'].repeat(freq_table['Frequency']))

    # Calculate IQR
    Q1 = freq_table.loc[freq_table['Frequency'].cumsum() >= (total_freq * 0.25)].iloc[0]['Midpoint']
    Q3 = freq_table.loc[freq_table['Frequency'].cumsum() >= (total_freq * 0.75)].iloc[0]['Midpoint']
    IQR = Q3 - Q1

    # Calculate standard error
    standard_error = std_dev / np.sqrt(freq_table['Frequency'].sum())

    return mean_grouped, mode, mode_class, median, skewness_grouped, kurtosis_value, IQR, std_dev, standard_error, median_class, variance

def main():
    st.title("Grouped Data Statistics")

    # Load dataset from CSV
    dataset = load_data()

    # Calculate age intervals and frequencies
    max_age = dataset['age'].max()
    intervals, labels = calculate_age_intervals(max_age)
    dataset['age_intervals'] = pd.cut(dataset['age'], bins=intervals, labels=labels, right=False)
    freq_table = dataset['age_intervals'].value_counts().reset_index()
    freq_table.columns = ['Age Interval', 'Frequency']
    freq_table['Age Interval'] = pd.Categorical(freq_table['Age Interval'], categories=labels, ordered=True)
    freq_table = freq_table.sort_values('Age Interval')

    # Filter out age intervals with zero frequency
    freq_table = freq_table[freq_table['Frequency'] > 0]

    # Calculate statistics
    mean_grouped, mode, mode_class, median_grouped, skewness_grouped, kurtosis_value, IQR, std_dev, standard_error, median_class, variance = calculate_grouped_statistics(freq_table)

    st.subheader("Age-Based Health Analysis: Gender, Weight, Height, and Diabetes Distribution")
    
    # Print results
    a1, a2, a3 = st.columns(3) 
    b1, b2, b3 = st.columns(3)   
    c1, c2, c3 = st.columns(3) 
    d1, d2 = st.columns(2)
    st.subheader("Grouped Data Statistics")
    a1.metric("Mean (Grouped Data):", f"{mean_grouped:.2f}")
    a2.metric("Mode (Grouped Data):", f"{mode:.2f}")
    a3.metric("Mode Class (Grouped Data):", mode_class)
    b1.metric("Median (Grouped Data):", f"{median_grouped:.2f}")
    b2.metric("Median Class (Grouped Data):", median_class)
    b3.metric("Skewness (Grouped Data):", f"{skewness_grouped:.2f}")
    c1.metric("Kurtosis (Grouped Data):", f"{kurtosis_value:.2f}")
    c2.metric("Interquartile Range (IQR) (Grouped Data):", f"{IQR:.2f}")
    c3.metric("Variance (Grouped Data):", f"{variance:.2f}")
    d1.metric("Standard Deviation (Grouped Data):", f"{std_dev:.2f}")
    d2.metric("Standard Error (Grouped Data):", f"{standard_error:.2f}")
    style_metric_cards(border_left_color="#e1ff8b", background_color="#222222")

    # Skewness visualization
    x = np.linspace(dataset['age'].min(), dataset['age'].max(), 100)
    p = norm.pdf(x, mean_grouped, std_dev)
    skew_fig = px.line(x=x, y=p, labels={'x': 'Age', 'y': 'Probability Density'})
    skew_fig.add_trace(go.Scatter(x=x, y=p, mode='lines', name='Normal Distribution'))
    skew_fig.update_layout(title="Skewness Visualization", xaxis_title="Age", yaxis_title="Probability Density",
                           plot_bgcolor='rgba(0,0,0,0)',  # Set background transparency
                           legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))  # Adjust legend position
    skew_fig.add_annotation(
        x=x[0],
        y=p[0],
        text=f"Skewness: {skewness_grouped:.2f}",
        showarrow=False,
        font=dict(color="red", size=12)
    )
    skew_fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray')  # Add gridlines on x-axis
    skew_fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray')  # Add gridlines on y-axis

    st.plotly_chart(skew_fig, use_container_width=True)

    # Display frequency table with cumulative frequency
    st.dataframe(freq_table)

if __name__ == "__main__":
    main()
