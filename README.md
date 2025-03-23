# UK_Road_Accident_Analysis

**Project XYZ**

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
The dataset used for this project contains detailed information about road accidents in the UK. It includes the following key features:

- **Date and Time**: The date and time when the accident occurred.
- **Location**: Latitude and longitude coordinates of the accident, along with the district or area.
- **Weather Conditions**: Information about weather conditions at the time of the accident (e.g., dry, wet, icy).
- **Road Surface Conditions**: Details about the road surface (e.g., dry, wet, snow, ice).
- **Road Type**: The type of road where the accident occurred (e.g., single carriageway, roundabout, slip road).
- **Severity**: The severity of the accident (e.g., slight, serious, fatal).
- **Number of Vehicles**: The number of vehicles involved in the accident.
- **Number of Casualties**: The number of people injured or killed in the accident.

The dataset spans multiple years and provides a comprehensive view of road accidents, enabling detailed analysis of trends, patterns, and factors contributing to accidents.

The data source can be found here:
[text](https://www.kaggle.com/datasets/charliescott556/uk-vehicle-accident-database-2019-2022/)



## Business Requirements

The primary goal of this project is to analyze road accident data in the UK to uncover patterns, trends, and insights that can help improve road safety. The specific business requirements are:

1. **Identify Seasonal Trends**:
   - Analyze whether accidents are more frequent during specific seasons (e.g., Winter) and determine the factors contributing to these trends.

2. **Assess Weather Impact**:
   - Investigate the relationship between weather conditions (e.g., wet, icy, or dry) and accident frequency or severity.

3. **Understand Multi-Vehicle Accidents**:
   - Determine whether multi-vehicle accidents result in a higher number of casualties compared to single-vehicle accidents.

4. **Compare Urban vs. Rural Areas**:
   - Analyze whether accidents in rural areas are more severe than those in urban areas.

5. **Provide Actionable Insights**:
   - Deliver insights that can help policymakers, road safety authorities, and urban planners make data-driven decisions to reduce accidents and improve road safety.

The user profile is the Department for Transport. As well as receiving insights on the above, they wanted the following specific questions answered:

## Hypothesis and how to validate?
1) Accidents are more frequent during Winter periods 
2) Accidents are more frequent during non-dry weather conditions.
3) Multi-vehicle accidents lead to a higher number of casualties.
4) Accidents in rural areas are more severe than urban.

## Project Plan

This project follows a structured approach to analyze UK road accident data and deliver actionable insights. The key steps in the project plan are as follows:

1. **Data Collection and Preparation**:
   - Source the dataset from [Kaggle](https://www.kaggle.com/datasets/charliescott556/uk-vehicle-accident-database-2019-2022/).
   - Clean and preprocess the data to handle missing values, inconsistencies, and outliers.
   - Perform feature engineering to extract relevant information (e.g., seasons from dates, accident severity categories).

2. **Exploratory Data Analysis (EDA)**:
   - Conduct basic and advanced visualizations to understand the dataset.
   - Identify trends, patterns, and potential relationships between variables (e.g., weather conditions and accident severity).

3. **Hypothesis Testing**:
   - Validate the hypotheses outlined in the "Business Requirements" section using statistical tests (e.g., Chi-Squared Test, Linear Regression).
   - Test relationships between variables such as weather conditions, road types, and accident severity.

4. **Data Visualization**:
   - Create visualizations to communicate insights effectively.
   - Use tools like Plotly and Matplotlib to generate interactive and static plots.

5. **Dashboard Development**:
   - Design and implement a dashboard to present key insights to both technical and non-technical audiences.
   - Ensure the dashboard is user-friendly and visually appealing.

6. **Modeling and Analysis**:
   - Use statistical and machine learning models (if applicable) to predict accident severity or identify key factors influencing accidents.
   - Evaluate model performance and interpret results.

7. **Insights and Recommendations**:
   - Summarize findings and provide actionable recommendations for improving road safety.
   - Highlight key insights for policymakers and stakeholders.

8. **Documentation and Deployment**:
   - Document the entire process, including challenges faced and solutions implemented.
   - Deploy the dashboard or application (if applicable) to a platform like Heroku for public access.

## The Rationale to Map the Business Requirements to the Data Visualisations

The visualizations in this project were designed to address the business requirements and hypotheses by providing clear and actionable insights. Below is the mapping of business requirements to the corresponding visualizations:

1. **Identify Seasonal Trends**:
   - **Visualization**: A line chart showing the number of accidents per month over the years.
   - **Rationale**: This visualization highlights seasonal patterns, such as whether accidents are more frequent during Winter months.

2. **Assess Weather Impact**:
   - **Visualization**: A bar chart comparing the number of accidents under different weather conditions (e.g., dry, wet, icy).
   - **Rationale**: This helps identify the relationship between weather conditions and accident frequency or severity.

3. **Understand Multi-Vehicle Accidents**:
   - **Visualization**: A stacked bar chart showing the number of casualties for single-vehicle vs. multi-vehicle accidents.
   - **Rationale**: This visualization demonstrates whether multi-vehicle accidents result in more casualties compared to single-vehicle accidents.

4. **Compare Urban vs. Rural Areas**:
   - **Visualization**: A box plot comparing accident severity in urban and rural areas.
   - **Rationale**: This visualization provides insights into whether accidents in rural areas are more severe than those in urban areas.

5. **Provide Actionable Insights**:
   - **Visualization**: A dashboard summarizing key findings, including accident trends, weather impact, and severity comparisons.
   - **Rationale**: The dashboard consolidates insights into a user-friendly format for policymakers and stakeholders.

Each visualization was chosen to effectively communicate the insights needed to meet the business requirements and validate the hypotheses.

## Analysis techniques used
* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques. Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Ethical considerations
* Were there any data privacy, bias or fairness issues with the data?
* How did you overcome any legal or societal issues?

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


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

### Test
