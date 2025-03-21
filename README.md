# UK Road Accident Analysis 

The objective of this project is to analyse road accidents in Birmingham and its surrounding areas and Coventry with its surrounding areas as well.
The objectives above will be achieved by the following activities (summarised - ETL, EDA, Visualisation, Dashboarding and Prediction analysis)
* Fetch data from Kaggle and save it in a folder.
* Preprocess the data.
* Clean the data using different methods.
* Perform Exploratory Data Analysis (EDA) for data distribution.
* Create various charts and graphs to gain insights to the data.
* Create and understand correlations of different variables of the data set.
* Generate visualisations of different variables using different libraries in Python.
* Use correlation heat maps to determine correlations to prove trends on variables.
* Use Tableau and Power Bi for Dashboarding.
* Use Logistics Regression for predictive analysis

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


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
1) Accidents are more frequent during Winter periods 
2) Accidents are more frequent during non-dry weather conditions.
### (I suggest changing 2 to non-dry accidents have a higher percentage of severe/fatal injuries, or drop it althougher)
3) Multi-vehicle accidents lead to a higher number of casualties.
4) Accidents in rural areas are more severe than urban.
5) Accident severity is dependent on light conditions. [view](jupyter_notebooks/06_Hypothesis_Testing_Categorical.ipynb)

## Project Plan
* Outline the high-level steps taken for the analysis.
* How was the data managed throughout the collection, processing, analysis and interpretation steps?
* Why did you choose the research methodologies you used?

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
* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques. Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Ethical considerations
- Data Privacy: The UK road accident dataset is anonymised, ensuring compliance with GDPR by removing personal identifiers like driver names and exact locations.

- Bias & Fairness:
    - Underreporting Bias: Minor accidents may be less frequently recorded.
    - Geographic Bias: More data from urban areas may lead to underrepresentation of rural accidents.
    - Class Imbalance: Fewer serious and fatal accidents compared to slight accidents.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

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
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 
* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.
