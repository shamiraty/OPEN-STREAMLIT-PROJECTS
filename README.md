# BUSINESS ANALYTICS WEB DASHBOARD
# DATA SCIENCE WEB DRIVEN WITH PYTHON AND STREAMLIT
## DESCRIPTIVE AND INFERENTIAL STATISTICS

![1](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/f7ad0f6c-16e0-4085-a129-4ede0b5b024c)

### Live Demo
[Live Demo](https://open-projects.streamlit.app/)

### YouTube
[Watch the video](https://www.youtube.com/watch?v=YkPxL-XLM7I)

# FEATURES:

| Topic                             | Description                         |
|-----------------------------------|-------------------------------------|
| 🏷 CO-VARIANCE                    | Measure of the joint variability of two variables. |
| 🏷 ADVANCED MULTIVARIATE REGRESSION | Regression techniques involving multiple predictors and response variables. |
| 🏷 TRENDS BY GEO-REFERENCING       | Analyze data trends based on geographic information. |
| 🏷 DESCRIPTIVE STATISTICS ANALYTICS | Summary and analysis of data with central tendency, dispersion, etc. |
| 🏷 MULTIPLE REGRESSION ANALYSIS    | Model the relationship between one dependent variable and multiple independent variables. |
| 🏷 SALES TRENDS BY DATE RANGE      | Analyze sales patterns over a specified time period. |
| 🏷 BUSINESS TARGET BY PROGRESS     | Evaluate business performance relative to targets. |
| 🏷 INTERACTIVE VISUALIZATION GRAPHS | Dynamic and user-interactive data visualizations. |
| 🏷 STATISTICS FOR GROUPED DATA       | Statistical analysis where data is organized into groups or intervals. |
| 🏷 STATISTICS FOR UNGROUPED DATA     | Statistical analysis of raw, ungrouped data values. |
| 🏷 ADVANCED PYTHON QUERY             | Techniques for complex data querying using Python. |
| 🏷 OUTLIER DETECTION TECHNIQUES      | Methods for identifying abnormal data points in datasets. |
| 🏷 HYPOTHESIS TESTING                | Statistical method to test assumptions or claims about a population. |
| 🏷 FREQUENCY DISTRIBUTION            | Representation of data showing the number of observations within intervals. |
| 🏷 NORMAL DISTRIBUTIONS              | Bell-shaped distribution that is symmetrical about the mean. |
| 🏷 PROBABILITY DISTRIBUTIONS         | Function that shows the likelihood of different outcomes in an experiment. |
| 🏷 LOGISTIC REGRESSION               | Model to estimate probabilities and model binary outcomes. |
| 🏷 ESTIMATION OF POPULATION          | Inference of population parameters based on sample data. |
| 🏷 PROBABILITY DENSITY               | Function describing the likelihood of a continuous random variable's outcome. |


## 1. DESCRIPTIVE STATISTICS FOR GROUPED DATA 

### 1. Data Loading
- **Data Source**: Loads dataset from a CSV file for analysis.

### 2. Age Interval Calculation
- **Purpose**: Creates age intervals (e.g., 0-10, 11-20) and labels for categorizing age data into discrete groups.

### 3. Frequency Table Creation
- **Purpose**: Generates a table counting occurrences within each age interval, facilitating grouped data analysis.

### 4. Grouped Statistical Calculations
- **Purpose**: Calculates essential statistics for grouped data, aiding in understanding data distribution:
  - **Mean**: Computes the weighted average midpoint of age intervals.
  - **Mode**: Identifies the most frequent age interval.
  - **Median**: Determines the midpoint interval in cumulative frequency.
  - **Variance and Standard Deviation**: Measures the spread of data points around the mean.
  - **Skewness and Kurtosis**: Assesses the symmetry and peakedness of the data distribution.
  - **Interquartile Range (IQR)**: Calculates the spread between the first and third quartiles.
  - **Standard Error**: Measures the precision of the sample mean.

### 5. Metric Display in Streamlit
- **Purpose**: Displays key grouped data statistics (mean, median, mode, etc.) to the user in an interactive dashboard.

### 6. Skewness Visualization
- **Purpose**: Plots a normal distribution curve to visualize data symmetry, with an annotation for skewness, allowing for a visual assessment of data distribution shape.

### 7. Frequency Table Display
- **Purpose**: Presents a frequency table with cumulative frequencies, providing insights into data distribution across age intervals.

## 2. DESCRIPTIVE STATISTICS  & DATA VISUALIZATION

# Data Science and Statistics Features

The following data science and statistical operations are performed in this code:

1. **Data Loading and Selection**  
   - Loads data from an Excel file (`data.xlsx`) and uses it for analytical processing.
   - Allows users to filter data by `Region`, `Location`, and `Construction` fields for customized analysis.

2. **Descriptive Analytics**  
   - Computes key summary statistics such as **Sum**, **Mode**, **Mean**, and **Median** for the `Investment` column.
   - Displays these metrics in the Streamlit interface for easy visualization.

3. **Data Visualization**  
   - **Histograms**: Visualizes the frequency distribution of variables in the dataset.
   - **Bar Chart**: Shows investments by `BusinessType`, providing a breakdown of investments by type.
   - **Line Chart**: Visualizes investments by `State`, showing trends across different states.
   - **Pie Chart**: Represents `Ratings` by `Region`, showing the proportion of ratings for each region.

4. **Target Tracking and Progress Bar**  
   - Defines a target for investment and calculates the current percentage toward this target.
   - Provides a progress bar to visually represent how close the current investment is to the target.

5. **Quartile Analysis**  
   - Uses a **box plot** to analyze the distribution of `Investment` by `BusinessType`, displaying quartiles and helping identify outliers.

6. **User Interface with Interactive Elements**  
   - Includes an interactive sidebar with options to navigate between different views (`Home`, `Progress`).
   - Enables selection of quantitative features for exploring distributions and trends.

## 3. HYPOTHESIS TESTING 

# Data Science and Statistical Operations in the Hypothesis Testing Dashboard

- **Data Loading and Cleaning**:
  - Reads data from an Excel file (`hypothesis.xlsx`).
  - Drops unnecessary columns to focus on relevant fields for hypothesis testing.

- **Hypothesis Formulation**:
  - Defines null and alternative hypotheses for comparing the mean revenues of Group A and Group B.

- **Confidence Level Setup**:
  - Sets a confidence level of 95% for statistical significance in hypothesis testing.

- **T-Test for Independent Samples**:
  - Conducts a t-test to compare means of two independent groups (Group A and Group B).
  - Calculates t-statistic and p-value for hypothesis evaluation.

- **Sample Statistics Calculation**:
  - Computes and displays sample mean and standard deviation for both groups.
  - Confirms sample size and enforces t-distribution usage only for samples smaller than 30.

- **Critical Value Determination**:
  - Calculates the critical value based on confidence level and sample size.

- **T-Distribution Curve Generation**:
  - Generates a probability density curve for visualizing the t-distribution.

- **Decision-Making**:
  - Compares computed t-statistic with critical value to decide whether to reject the null hypothesis.

- **Visualization of Results**:
  - Displays t-distribution curve with annotated critical value, t-statistic, and rejection region.
  - Uses visual aids (vertical lines, filled regions) to highlight decision boundaries and critical regions.

- **Summary Metrics Display**:
  - Shows computed values and critical values in a dashboard format.
  - Presents a sample size and statistical metrics in a well-organized layout using Streamlit components.


## 4.  ADVANCED LINEAR REGRESSION

# Data Science and Statistical Analysis Performed

## 1. Data Loading and Selection
- **Data Source:** Loaded from CSV file (`advanced_regression.csv`).
- **Feature Columns:** `interest_rate`, `unemployment_rate`, `index_price`.
- **Filtering:** Data is filtered based on user-selected year and month.

## 2. Exploratory Data Analysis (EDA)
### Correlation Analysis:
- Used `sns.regplot` to visually explore relationships between features.
- Calculated and displayed correlation matrix for the variables.

### Visualizing Relationships:
- Regression plots show the relationships between `interest_rate` and `unemployment_rate`, `interest_rate` and `index_price`.
- Box plots detect outliers in the dataset.

### Variable Distributions:
- Displayed histograms for variable frequency distributions.
- Used `sns.pairplot` to examine pairwise relationships.

## 3. Handling Missing Data
- Checked for missing values and displayed the count of `NaN` entries in each column.
- Provided descriptive statistics (mean, standard deviation, etc.) for each variable.

## 4. Data Preprocessing
### Splitting the Data:
- Split the data into training and testing sets using `train_test_split`.

### Standardization:
- Applied standardization using `StandardScaler` to scale features.

## 5. Modeling
### Multiple Linear Regression Model:
- Built a linear regression model using `LinearRegression` from `sklearn`.
- Used cross-validation to evaluate model performance.

### Prediction:
- Predicted the target variable (`index_price`) on the test dataset.

## 6. Model Evaluation
### Performance Metrics:
- Calculated and displayed **Mean Squared Error (MSE)**, **Mean Absolute Error (MAE)**, and **Root Mean Squared Error (RMSE)**.

### R² and Adjusted R²:
- Calculated and displayed the **R²** and **Adjusted R²** values for model performance.

### Residuals Analysis:
- Computed residuals and visualized them using a normal distribution curve to check the error distribution.

## 7. Statistical Analysis
- Used **OLS (Ordinary Least Squares)** regression from `statsmodels` to obtain detailed model insights, including coefficients and p-values.


## 5. CO-VARIANCE

# Data Science and Statistical Operations in the Dashboard

- **Data Loading**: Loads data from an Excel file, allowing for further statistical operations and visualizations.
  
- **Feature Selection**: Provides a feature selection for `X` variable, enabling dynamic analysis of various numerical features against the target variable.

- **Statistical Model Fitting**: Fits an Ordinary Least Squares (OLS) regression model to examine the relationship between the selected `X` feature and the target variable (`Projects`).

- **Key Statistical Metrics Calculation**:
  - **Intercept**: Displays the intercept term of the model, representing the baseline effect on `Projects`.
  - **R-Squared**: Shows the R-squared value, providing insight into the model's explanatory power.
  - **Adjusted R-Squared**: Adjusts for the number of predictors to gauge model fit accuracy.
  - **Standard Error**: Provides the standard error, indicating the precision of the intercept estimate.

- **Predictions and Residuals Calculation**: Calculates model predictions and residuals for further analysis.

- **Data Visualization**:
  - **Line of Best Fit Plot**: Generates a scatter plot with a line of best fit to visualize the relationship between the selected `X` feature and `Projects`, assessing the model fit visually.
  - **Grid and Border Customization**: Customizes plot appearance for better interpretability.


## 6. DESCRIPTIVE STATISTICS  FOR UNGROUPED DATA

# Data Science and Statistical Analysis Steps

1. **Data Loading**
   - Load dataset from a CSV file for analysis.

2. **Quartile and IQR Calculation**
   - Calculate the 1st Quartile (Q1), 3rd Quartile (Q3), and Interquartile Range (IQR) for understanding the spread of the dataset.

3. **Basic Statistics Computation**
   - Determine minimum, maximum, and median values to summarize the dataset's range and central tendency.

4. **Ogives Plotting**
   - Generate Less Than and Greater Than Ogives to visualize cumulative frequency distribution.
   - Add a vertical line and annotation for the median value to highlight central tendency in the plot.

5. **Display Statistics in Streamlit Dashboard**
   - Display quartiles, IQR, min, max, and median values in an interactive layout for user insights.
   - Apply styling to metrics for improved readability and visual appeal.

6. **Interactive Visualization**
   - Present the ogives plot in Streamlit to allow for intuitive data exploration.


## 7. DATA VISUALIZATION

# Data Science and Statistics Features

The following data science and statistical operations are performed in this code:

1. **Data Loading and Selection**  
   - Loads data from an Excel file (`data.xlsx`) and uses it for analytical processing.
   - Allows users to filter data by `Region`, `Location`, and `Construction` fields for customized analysis.

2. **Descriptive Analytics**  
   - Computes key summary statistics such as **Sum**, **Mode**, **Mean**, and **Median** for the `Investment` column.
   - Displays these metrics in the Streamlit interface for easy visualization.

3. **Data Visualization**  
   - **Histograms**: Visualizes the frequency distribution of variables in the dataset.
   - **Bar Chart**: Shows investments by `BusinessType`, providing a breakdown of investments by type.
   - **Line Chart**: Visualizes investments by `State`, showing trends across different states.
   - **Pie Chart**: Represents `Ratings` by `Region`, showing the proportion of ratings for each region.

4. **Target Tracking and Progress Bar**  
   - Defines a target for investment and calculates the current percentage toward this target.
   - Provides a progress bar to visually represent how close the current investment is to the target.

5. **Quartile Analysis**  
   - Uses a **box plot** to analyze the distribution of `Investment` by `BusinessType`, displaying quartiles and helping identify outliers.

6. **User Interface with Interactive Elements**  
   - Includes an interactive sidebar with options to navigate between different views (`Home`, `Progress`).
   - Enables selection of quantitative features for exploring distributions and trends.

## 8. LINEAR REGRESSION

# Predictive Analytics Dashboard: Multiple Regression Analysis

### 1. **Data Loading and Preprocessing**:
- The dashboard loads an Excel dataset (`regression.xlsx`) containing information on `Dependant`, `Wives`, and `Projects`.
- Extracts the independent variables (`Dependant` and `Wives`) and the dependent variable (`Projects`) for use in regression analysis.

### 2. **Model Fitting and Prediction**:
- A **Linear Regression** model is trained on the dataset using `Dependant` and `Wives` to predict the `Projects` (dependent variable).
- Predictions are made using the trained model and stored for further analysis.

### 3. **Regression Coefficients**:
- The **Intercept (Bo)** and **Coefficients (B1, B2)** for the independent variables are calculated and displayed. These represent the linear relationship between the predictors and the dependent variable.

### 4. **Model Evaluation Metrics**:
- **R-squared (R²)**: Measures the proportion of variance in the dependent variable explained by the independent variables.
- **Adjusted R-squared**: Adjusts R² for the number of predictors in the model, preventing overfitting.
- **Sum of Squared Errors (SSE)**: Calculates the total error between the predicted and actual values.
- **Sum of Squared Regression (SSR)**: Measures the variation explained by the model.

### 5. **Prediction Table**:
- Displays a table with the actual and predicted `Projects` (Y) values, along with the SSE and SSR values for each data point.

### 6. **Residual Analysis**:
- **Residuals**: The difference between the actual and predicted values of `Projects` is calculated.
- A scatter plot of the residuals versus the predicted values is displayed to visualize model fit.
- A **Kernel Density Estimation (KDE)** plot of the residuals is shown to analyze their distribution.

### 7. **User Input and Prediction**:
- Users can input new values for `Dependant` and `Wives` in a sidebar form.
- Upon submission, the model predicts the number of `Projects` for the provided inputs and displays the result.

### 8. **Download Option**:
- The user can download the dataset with the actual values, predicted values, SSE, and SSR as a CSV file.

### 9. **Visualizations**:
- **Regression Line and Scatter Plot**: Visualizes the relationship between actual and predicted values, including the best fit line.
- **Residual Plot**: Shows the distribution of residuals using a KDE plot.

## 9. SALES ANALYTICS { CASE STUDY }
# Data Science and Statistics Overview for Sales Analytics Page

## 1. Data Import and Processing
- **Dataset Loading**: A CSV file (`sales.csv`) is read into a pandas DataFrame for analysis.
- **Date Filtering**: Users can filter the dataset by a date range (start and end dates). The data is filtered based on the `OrderDate` column to display relevant sales data.
- **Data Exploration**: A DataFrame explorer is used to interactively view and filter the dataset, making it easier for users to explore the data.

## 2. Descriptive Analytics
- **Metrics Calculation**:
  - **Total Products in Inventory**: Count of `Product` entries to display the number of inventory items.
  - **Total Price Sum**: The sum of all `TotalPrice` values is displayed to give an overall view of sales revenue.
  - **Price Range Analysis**:
    - Maximum and minimum price for products are calculated and displayed.
    - Price range (difference between the maximum and minimum prices) is calculated.
- These metrics provide key insights into inventory and sales data.

## 3. Data Visualization
- **Dot Plot**: A scatter plot is used to visualize the relationship between `Product` and `TotalPrice`. Each point represents a product with its corresponding total price, and products are color-coded by their category.
- **Bar Graph**: A bar chart is used to display the relationship between `Product` and `UnitPrice`. The chart aggregates `UnitPrice` over months to show trends in pricing.
- **Scatter Plot**: A scatter plot is created based on user-selected features. It visualizes relationships between categorical (qualitative) data (`feature_x`) and numerical (quantitative) data (`feature_y`).
- **Bar Chart of Quantities**: A bar chart visualizes the total quantity sold for each product, helping to analyze product demand.

## 4. Interactive User Interface
- **Date Range Selection**: Users can select a date range from the sidebar, allowing them to filter sales data dynamically.
- **Feature Selection**: Users can select features for the x and y axes to explore relationships in the data through scatter plots.
- **Data Table**: The filtered dataset is displayed interactively for further analysis.

## 5. Statistical and Business Insights
- **Price Range Insights**: The metrics calculated (maximum, minimum, range) help users identify high-value and low-value products, which is critical for pricing strategies.
- **Sales Trend Analysis**: The dot plot and bar charts help identify trends in product sales, such as which products have higher sales and which products are more expensive.
- **Business Metrics**: The overall revenue and inventory metrics provide insights into the health of the business and help with decision-making.

## Conclusion
This page is focused on descriptive analytics and basic statistics. The main tasks involve:
- Data cleaning and filtering.
- Displaying key business metrics related to product pricing and sales volume.
- Visualizing the relationship between various features such as product prices and quantities.
- Providing interactive tools for users to explore the dataset and extract insights.

# OTHER VIDEO SERIES:

### Data Science Web Development Job Recommendation System

1. **Part 1**: [Introduction](https://youtu.be/yzp2HIZRyHA)
2. **Part 2**: [Admin Theme](https://youtu.be/yzU4LapsCpk)
3. **Part 3**: [Model Training and Prediction](https://youtu.be/fLZCsJHaYeM)
4. **Part 4**: [View, URL, and Template Rendering](https://youtu.be/7WdS3JpjQZM)
5. **Part 5**: [How to Generate 10000 Fake Dataset CSV](https://youtu.be/KoKzEuweae8)
6. **Episode 6**: [Project Overview](https://youtu.be/R1sdxL51X00)

# OTHER STREAMLIT VIDEO SERIES

1. **Business Analytics Web Dashboard**
   - [Live Demo](https://open-projects.streamlit.app/)
   - [YouTube](https://youtu.be/YkPxL-XLM7I)

2. **Analytics Website Dashboard**
   - [Live Demo](https://open-projects.streamlit.app/)
   - [YouTube](https://youtu.be/pWxDxhWXJos)

3. **Logistic Multiple Regression Analytics Web**
   - [YouTube](https://youtu.be/WV5WhbeJ1TA)
   - [Live Demo](https://open-findings.streamlit.app/)

4. **Normal Probability Distribution Analytics Web**
   - [Live Demo](https://normal-distribution.streamlit.app/)
   - [YouTube](https://youtu.be/9JhRtXUdUYs)

5. **Python: Query Operations**
   - [Live Demo](https://python-query.streamlit.app/)
   - [YouTube](https://youtu.be/n6-5l7dzSlk)

6. **Python: Binomial Probability Distributions**
   - [Live Demo](https://binomial-probability.streamlit.app/)
   - [YouTube](https://youtu.be/fZPqU320YX4)

7. **Hypothesis Testing T Distribution Curve**
   - [Live Demo](https://hypothesis.streamlit.app/)
   - [YouTube](https://youtu.be/VvoeqYPyjR0)

8. **Frequency Distribution Table**
   - [Live Demo](https://frequency-distributions.streamlit.app/)
   - [YouTube](https://youtu.be/bGi2zdezJQg)

9. **Geo Referencing Business Trends**
   - [Live Demo](https://open-analytics.streamlit.app/)
   - [YouTube](https://youtu.be/RRZ4l6JeNGI)

10. **Multiple Linear Regression Web Project**
    - [Live Demo](https://business-analytical.streamlit.app/)
    - [YouTube](https://youtu.be/VeP0c-ZPkD8)

11. **Python: Web Dashboard: DashPlotly Framework and Dash**
    - [Live Demo](https://python13.onrender.com/)
    - [YouTube](https://youtu.be/EMA75EEORoI)

12. **Python: Web Dashboard using DashPlotly Framework**
    - [Live Demo](https://project-fpy1.onrender.com/)
    - [YouTube](https://youtu.be/5SbIGjhkez0)

13. **Python: Multiple Linear Regression**
    - [Live Demo](https://business-force.streamlit.app/)
    - [YouTube](https://youtu.be/y5GRNibPiW4)

14. **Logistic Regression Analysis**
    - [Live Demo](https://open-projects.streamlit.app/)
    - [YouTube](https://youtu.be/5ab1L5li8z4)

15. **PygWalker Graph Creator**
    - [Live Demo](https://open-projects.streamlit.app/)
    - [YouTube](https://youtu.be/JeoYZkmeYTo)

16. **Sales Analytics Web Dashboard**
    - [Live Demo](https://open-projects.streamlit.app/)
    - [YouTube](https://youtu.be/uDuPM4xfPlw)

17. **Analytics Dashboard with MySQL**
    - [Live Demo](https://open-projects.streamlit.app/)
    - [YouTube](https://youtu.be/rJzBNm0rb0g)

18. **Business Intelligent Analytics Web Dashboard**
    - [Live Demo](https://open-projects.streamlit.app/)
    - [YouTube](https://youtu.be/mDJ-sKB7DvE)

19. **Descriptive Analytics Web Dashboard 1**
    - [Live Demo](https://open-projects.streamlit.app/)
    - [YouTube](https://youtu.be/sIqBA0PhzGQ)

20. **Descriptive Analytics Web Dashboard 2**
    - [Live Demo](https://shamiraty-numbersummary-percentiles-main-bng7ov.streamlit.app/)
    - [YouTube](https://youtu.be/U7vf-DB_KmQ)

21. **Analytics Dashboard Website with Graphs 3**
    - [Live Demo](https://open-projects.streamlit.app/)
    - [YouTube](https://youtu.be/-cg3qPhI74s)

22. **Add new Record to Excel file via Web Interface**
    - [Live Demo](https://shamiraty-add-data-to-excel-streamlit-main-4mef19.streamlit.app/)
    - [YouTube](https://youtu.be/-3q2rwuy99g)

23. **CrossTabulation Web App**
    - [Live Demo](https://shamiraty-crosstabulation-main-b2c61u.streamlit.app/)
    - [YouTube](https://youtu.be/1fnq4CzezxQ)



![2](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/e70c9c86-926a-48e0-ae5e-ad51fec5dad6)
![3](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/b27bfd87-11d3-4500-9e14-863bfc763af5)
![4](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/f7f2e2c0-5477-4558-9f6f-83cdc8edad7c)
![5](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/303e16cb-c7a8-4b0f-a3ff-e786af775723)
![20](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/4516cc5f-7a05-4b95-ab24-69355a7170ee)
![19](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/1923f10f-7c46-493f-bafe-ba434005a35a)
![18](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/97664783-cc8b-412f-b0d7-c5bd442d471a)
![17](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/d2556ad5-e3dc-4e7f-bd86-8955275a6b4c)
![9](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/3e46e3cb-3018-4251-a44e-44da74ee96e6)!
![16](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/98fa0007-09d6-4b40-99b4-58f2373e34a9)
[10](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/7119ce23-86b4-47c0-8d5c-3b0bda089b64)
![8](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/1b13bbaf-b877-4064-9200-99e4a4fe60b6)
![7](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/44309344-5e24-45e7-ba21-3029f9af4818)
![6](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/ccef4636-32cd-4d5c-9f51-bc6657fcc4fe)
![26](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/4b24f61d-197c-488c-ae51-95f2dc85fa36)
![25](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/3a96cc6e-142b-4881-893e-41435566ba96)
![24](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/bd72b0e9-f33f-4f9e-9f66-c75842e0a244)
![23](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/22282a04-f55b-4e7c-bcac-6c66f6afa1dd)
![22](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/afe48cce-a5ed-4b1d-9937-3799a7df2a4a)
![21](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/06a7fbd4-c5d5-47d6-a01d-ebf520e3eb5e)
![14](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/584c7444-c463-4ce0-a2a9-3faf3f72284b)
![13](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/b1094b21-0760-4d9b-9d9d-ebe1f21bc08f)
![12](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/819035cf-67a6-4086-860c-786f213e2123)   
![15](https://github.com/shamiraty/OPEN-STREAMLIT-PROJECTS/assets/129072179/e8eb4977-8775-4921-8a82-9a71a1ecb0b3)

### Contact Information

#### WhatsApp
- +255675839840
- +255656848274

#### YouTube
[YouTube Channel](https://www.youtube.com/channel/UCjepDdFYKzVHFiOhsiVVffQ)

#### Telegram
- +255656848274
- +255738144353

#### PlayStore
[PlayStore Developer Page](https://play.google.com/store/apps/dev?id=7334720987169992827&hl=en_US&pli=1)

#### GitHub
[GitHub Profile](https://github.com/shamiraty/)


