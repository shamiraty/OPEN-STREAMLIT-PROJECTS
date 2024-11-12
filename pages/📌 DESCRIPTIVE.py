import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(layout="wide")

def load_data():
    return pd.read_csv('dataset.csv')

st.sidebar.image("logo2.png", caption="EmployeeEcho Insights")

def calculate_statistics(data):
    # Compute basic statistics
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    min_val = np.min(data)
    max_val = np.max(data)
    median_val = np.median(data)
    
    return Q1, Q3, IQR, min_val, max_val, median_val

def plot_ogives(data, median_val):
    sorted_data = np.sort(data)
    cumulative_freq = np.arange(1, len(sorted_data) + 1)
    total_freq = len(data)
    
    # Less than ogive
    less_than_ogive = cumulative_freq / total_freq

    # Greater than ogive
    greater_than_ogive = (total_freq - cumulative_freq + 1) / total_freq

    fig = go.Figure()

    # Plot Less Than Ogive
    fig.add_trace(go.Scatter(
        x=sorted_data,
        y=less_than_ogive,
        mode='lines+markers',
        name='Less Than Ogive'
    ))

    # Plot Greater Than Ogive
    fig.add_trace(go.Scatter(
        x=sorted_data,
        y=greater_than_ogive,
        mode='lines+markers',
        name='Greater Than Ogive'
    ))

    # Add vertical red line at the median
    fig.add_shape(
        type="line",
        x0=median_val,
        y0=0,
        x1=median_val,
        y1=1,
        line=dict(color="red", width=2),
        xref="x",
        yref="paper"
    )

    # Add annotation for median value
    fig.add_annotation(
        x=median_val,
        y=0.5,  # Middle of the plot
        text=f"Median: {median_val:.2f}",
        showarrow=True,
        arrowhead=2,
        ax=40,  # Adjust the position of the label
        ay=0,
        font=dict(color="red", size=12),
        bgcolor="white"
    )

    fig.update_layout(
        title='Less Than and Greater Than Ogives with Median',
        xaxis_title='Age',
        yaxis_title='Cumulative Frequency',
        plot_bgcolor='rgba(0,0,0,0)',  # Set background transparency
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)  # Adjust legend position
    )
    
    return fig

def main():
    st.title(" Age Analysis - Ungrouped Data")

    # Load dataset from CSV
    dataset = load_data()
    
    # Extract ungrouped data
    data = dataset['age']

    # Calculate statistics
    Q1, Q3, IQR, min_val, max_val, median_val = calculate_statistics(data)

    # Plot Ogives
    ogives_fig = plot_ogives(data, median_val)

    a1, a2, a3 = st.columns(3) 
    b1, b2 = st.columns(2)  
    # Display results
    st.subheader("Ungrouped Data Statistics")
    a1.metric("1st Quartile (Q1):", f"{Q1:.2f}")
    a2.metric("3rd Quartile (Q3):", f"{Q3:.2f}")
    a3.metric("Interquartile Range (IQR):", f"{IQR:.2f}")
    b1.metric("Minimum Value:", f"{min_val:.2f}")
    b2.metric("Maximum Value:", f"{max_val:.2f}")
    style_metric_cards(border_left_color="#e1ff8b",background_color="#222222")

    st.subheader("Visualizations")
    st.plotly_chart(ogives_fig, use_container_width=True)

if __name__ == "__main__":
    main()
