# UK Road Accident Analysis 

The objective of this project is to analyse road accidents in Birmingham and its surrounding areas and Coventry with its surrounding areas as well.
The objectives above will be achieved by the following activities (summarised - ETL, EDA, Visualisation, Dashboarding and Prediction analysis) detailed below.
* Fetch data from Kaggle and save it in a folder.
* Preprocess the data.
* Clean the data using different methods.
* Perform Exploratory Data Analysis (EDA) for data distribution.
* Create various charts and graphs to gain insights to the data.
* Create and understand correlations of different variables of the data set.
* Generate visualisations of different variables using different libraries in Python.
* Use correlation heat maps to determine correlations to prove trends on variables.
* Use Tableau, Streamlit and Power Bi for Dashboarding.
* Use Logistics Regression for predictive analysis

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Links to Deployed Dashboards

* [Tableau](https://public.tableau.com/app/profile/julian.colling/viz/Birmingham_Area_Accidents_Dashboard/RoadAccidentDashboard)

* [Streamlit](https://uk-road-accident-analysis-dashboard.streamlit.app/)


## Dataset Content
* The data set contains 13 columns of variables with 31511 rows. The variables are as follows
* Accident_Severity	
* Accident Date	
* Latitude	
* Light_Conditions	
* District Area	
* Longitude	
* Number_of_Casualties	
* Number_of_Vehicles	
* Road_Surface_Conditions	
* Road_Type	
* Urban_or_Rural_Area	
* Vehicle_Type
* The origional data set was found in Kaggle: https://www.kaggle.com/datasets/nezukokamaado/road-accident-casualties-dataset

## Business Requirements

* Identify accident-prone areas to aid in infrastructure improvement.

* Analyse causes and patterns of accidents to support policy recommendations.

* Evaluate the impact of road safety measures over time.

* Provide data-driven insights for law enforcement, city planners, and policymakers.

* Predict future accident trends using historical data and machine learning models.

* Obtain historical accident data from government agencies, police reports, and transport authorities.

* Collect data points including date, time, location, road type, weather conditions, accident severity, vehicle types, and driver details (age, gender, license type, etc.).

* Integrate GIS (Geographical Information Systems) for spatial analysis.

## Hypothesis and how to validate?
1) Accidents are more frequent during Winter periods. (Dispproved)[view](jupyter_notebooks/07_Hypothesis Testing - Temporal Data.ipynb) 
2) Accidents are more frequent during non-dry weather conditions.[view](jupyter_notebooks/04_EDA_Advanced .ipynb) ([view](jupyter_notebooks/03_EDA_Basic.ipynb)
3) Multi-vehicle accidents lead to a higher number of casualties.[view](jupyter_notebooks/03_EDA_Basic.ipynb)
4) Accidents in rural areas are more severe than urban.[view](jupyter_notebooks/05_Hypothesis Testing - Numerical Variables.ipynb)
5) Accident severity is dependent on light conditions. [view](jupyter_notebooks/06_Hypothesis_Testing_Categorical.ipynb)

[test](<jupyter_notebooks/05_Hypothesis Testing - Numerical Variables.ipynb>)

## Project Plan
The project plan was executed by the following process
* Kanban planning: The kanban project planning is used to plan for tasks and tracking of tasks as the project progresses.
* Data Collection: Load the dataset from the Kaggle.
* Save the file in the folder in the directory
* Data Cleaning: Handle missing values, check duplicates, and standardise formats.Processing, analysis and interpretation of data, some of the methods used are like df.info(), df.isnull().sum().
* Data Transformation: Nothing to clean as the dataset had no duplicates or missing values.
* Save the cleaned file in a new folder in the directory.
* Analysis: Perform exploratory data analysis, trend analysis, and correlation analysis
* Modeling: Logistics Regression.
* Visualization: Build dashboards from Power Bi to present insights and predictions.

## The rationale to map the business requirements to the Data Visualisations
- Business Requirement: Identify accident-prone areas to aid in infrastructure improvement
- Rationale: Visualising accident counts by district helps pinpoint high-risk areas, guiding targeted infrastructure improvements.
    - notebook: `03_EDA_Basic`
    - section heading: `Bar Chart for Districts `

<br> 

- Business Requirement: Predict future accident trends using historical data and machine learning models.
- Rationale: Machine learning models analyse historical patterns to forecast accident trends, supporting proactive safety measures and resource allocation.
    - notebook: `09_Machine_Learning`
    - current status: Further model improvements were unsuccessful. Exploring LightGBM, ensemble methods, or better handling class imbalance may be needed.


## Analysis techniques used
Data Analysis methods
*EDA Non Graphical methods were used to analyse the data to understand parameters like the mean, median and standard deviation etc.
* EDA Basic graphs and Charts like Bar charts, Histograms, scatter plts and correlation heatmaps were utilised for further analysis.
EDA Advanced 
Pandas, Matplot lib and Plotly were utilised to get high quality visualisations.
* Use of AI Tools: ChatGPT was used for brainstorming business requirements and personification of the prompts. GitHub Copilot was used to prompt for hypotheses and improving code.
## Ethical considerations
- Data Privacy: The UK road accident dataset is anonymised, ensuring compliance with GDPR by removing personal identifiers like driver names and exact locations.

- Bias & Fairness:
    - Underreporting Bias: Minor accidents may be less frequently recorded.
    - Geographic Bias: More data from urban areas may lead to underrepresentation of rural accidents.
    - Class Imbalance: Fewer serious and fatal accidents compared to slight accidents.

## Dashboard Design
The Dash boards used are:
* Tableau
* Power Bi
* Streamlit
All the dashboard content will be presented by power point to the stakeholders

## Machine Learning
* Data Preprocessing: Load, clean, and encode the dataset; define the target variable (Accident_Severity).

* Modeling: Use multinomial logistic regression, Random Forest, XGBoost models with a preprocessing pipeline.

* Training & Evaluation: Train the model, make predictions, and assess performance using precision, recall, and F1-score.

* Challenges & Improvements: Address class imbalance using SMOTE.

* SMOTE Implementation: Apply SMOTE and re-train the model for better results.

## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

1. Due to the high class imbalance in the target variable 'Accident_Severity', the model was biased towards the majority class. We attempted to use SMOTE, but further investigation into other resampling techniques is needed

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Main Data Analysis Libraries
All the libraries used in this project are below
* numpy==1.26.1
* pandas==2.1.1
* matplotlib==3.8.0
* seaborn==0.13.2
* ydata-profiling==4.12.0 # can be removed from requirements before deployment
* plotly==5.17.0
* ppscore==1.1.0 # can be removed from requirements before deployment
* streamlit==1.40.2
* feature-engine==1.6.1
* imbalanced-learn==0.11.0
* scikit-learn==1.3.1
* xgboost==1.7.6
* yellowbrick==1.5 # can be removed from requirements before deployment
* Pillow==10.0.1 # can be removed from requirements before deployment
* nbformat>=4.2.0

## Credits 
* Credit goes to all the team members who worked tirelesly to finish the project. Special credit goes to Maha who led with support in resolving Repository issues with branches and git pulls.

## Acknowledgements (optional)
* Thank you to all the team members.
