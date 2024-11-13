import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm
from streamlit_extras.metric_cards import style_metric_cards


st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")
st.header("STANDARD NORMAL DISTRIBUTION  Z~(0,1)")  
st.write("RANDOM VARIABLE & PROBABILITY DISTRIBUTIONS")

theme_plotly = None 

#sidebar
html_code = '''
<iframe src="https://free.timeanddate.com/clock/i95di01a/n71/szw160/szh160/hocfff/hbw6/cf100/hgr0/hcw2/hcd88/fan2/fas20/fdi70/mqc000/mqs3/mql13/mqw4/mqd94/mhc000/mhs3/mhl13/mhw4/mhd94/mmc000/mml5/mmw1/mmd94/hwm2/hhs2/hhb18/hms2/hml80/hmb18/hmr7/hscf09/hss1/hsl90/hsr5" frameborder="0" width="160" height="160"></iframe>

'''
st.sidebar.markdown(html_code, unsafe_allow_html=True)

# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def main():
    
    file = pd.read_excel("normal_distr.xlsx")
    if file is not None:
        df = file
        marks_column = df['Marks']

        # Convert to integers for the slider
        marks_min = int(marks_column.min())
        marks_max = int(marks_column.max())
        marks_mean = int(marks_column.mean())

        # Sidebar slider for selecting X value
        x_value = st.sidebar.slider('Select X value', marks_min, marks_max, marks_mean)

        col1,col2=st.columns(2)
        # Calculations
        mean = np.mean(marks_column)
        std_dev = np.std(marks_column)
        z_score = (x_value - mean) / std_dev
        probability = norm.cdf(z_score)
        
        
        with st.expander("VIEW ESTIMATION PARAMETERS"):
         # Display computed information
         col1,col2,col3,col4,col5=st.columns(5)
         col1.metric(f"Population Mean: ",value=f"{mean:,.4f}")
         col2.metric(f"Selected X: ",value=x_value)
         col3.metric(f"Z-score value: ",value=f"{z_score:,.4f}")
         col4.metric(f"Probability: ",value=f"{probability:,.4f}")
         col5.metric(f"Standard Dev: ",value=f"{std_dev:,.4f}")
         style_metric_cards()

         
       # Create Z-score graph using Plotly
        z_values1 = np.linspace(-3, 3, 1000)
        prob_values1 = norm.pdf(z_values1)
        z_fig = px.line(x=z_values1, y=prob_values1, labels={'x': 'Z-score', 'y': 'Probability Density'})
        z_fig.add_trace(go.Scatter(x=[z_score], y=[norm.pdf(z_score)], mode='markers', marker=dict(color='red', size=10), name='Z-score value'))

        if z_score > 0:
            z_fig.add_vrect(x0=z_score, x1=3, fillcolor='rgba(0,100,80,0.2)', line_width=0, opacity=0.5, name='Shaded Area')
        else:
            z_fig.add_vrect(x0=-3, x1=z_score, fillcolor='rgba(0,100,80,0.2)', line_width=0, opacity=0.5, name='Shaded Area')

        z_fig.add_vline(x=0, line=dict(color='red', dash='dash'), name='Mean')  # Add line for mean at Z = 0
        z_fig.update_layout(title='', xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))
        
         
        # Standardize marks
        standardized_marks = (marks_column - mean) / std_dev
        df['Standardized Marks'] = standardized_marks

        
        z_values = np.linspace(-3, 3, 1000)
        prob_values = norm.pdf(z_values)
        standardized_marks = px.line(x=z_values, y=prob_values, labels={'x': 'Z-score', 'y': 'Probability Density'})
        standardized_marks.add_trace(go.Scatter(x=[z_score], y=[norm.pdf(z_score)], mode='markers', marker=dict(color='red', size=10), name='Z-score value'))
        standardized_marks.add_annotation(x=np.mean(z_values), y=max(prob_values), text="Mean", showarrow=True, arrowhead=1, xshift=10)
        standardized_marks.add_annotation(x=np.median(z_values), y=max(prob_values), text="Median", showarrow=True, arrowhead=1, xshift=10)
        standardized_marks.add_annotation(x=0, y=max(prob_values), text="Mode", showarrow=True, arrowhead=1, xshift=10)
        standardized_marks.add_annotation(x=np.std(z_values), y=max(prob_values), text="Standard Deviation", showarrow=True, arrowhead=1, xshift=10)
        standardized_marks.add_vline(x=np.mean(z_values), line_dash="dash", line_color="red", name='Mean')
        standardized_marks.add_vline(x=np.median(z_values), line_dash="dash", line_color="blue", name='Median')
        standardized_marks.add_vline(x=0, line_dash="dash", line_color="green", name='Mode')
        standardized_marks.add_vline(x=np.std(z_values), line_dash="dash", line_color="orange", name='Standard Deviation')
        standardized_marks.update_layout(title='', xaxis=dict(showgrid=True), yaxis=dict(showgrid=True), legend=dict(orientation="h", y=1.1, x=0.5))
               
        with st.expander("VIEW NORMAL CURVES"):
         p1,p2=st.columns(2)
         with p1:
          st.info("Standardized Marks Distribution")
          st.plotly_chart(standardized_marks,use_container_width=True)
    
         with p2:
          st.info("Probability of selected X :")
          st.plotly_chart(z_fig,use_container_width=True)

        with st.expander("STANDARDIZED STUDENT MARKS"):
         st.info("Standardized Marks Table:")
         showData=st.multiselect('Filter: ',df.columns,default=["fullname","gender","Marks","Probability","Standardized Marks"])
         st.dataframe(df[showData],use_container_width=True)

if __name__ == "__main__":
    main()


# HTML code for the analog clock
import base64
def read_pdf(file_path):
    with open(file_path, "rb") as file:
        contents = file.read()
    return contents

def pdf():
    file_path = "Z table.pdf"   
    pdf_contents = read_pdf(file_path)
    b64 = base64.b64encode(pdf_contents).decode('utf-8')
    href = f'<a href="data:application/pdf;base64,{b64}" download="downloaded_file.pdf">Download PDF file</a>'
    st.markdown(href, unsafe_allow_html=True)


# Define Z-score values
z_scores = np.around(np.arange(-3.4, 3.5, 0.1), decimals=2)

# Create a dictionary to store Z-table values
z_table_values = {z: [round(norm.cdf(z), 4) for z in z_scores] for z in z_scores}

# Create a DataFrame to display Z-table values
z_table = pd.DataFrame(z_table_values, index=z_scores)


with st.expander("VIEW Z TABLE"):
 pdf()
 st.dataframe(z_table,use_container_width=True)

