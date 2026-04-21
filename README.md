# PRODIGY_DS_02
## Task-02: Data Cleaning and Exploratory Data Analysis (EDA)

### Objective
Perform data cleaning and exploratory data analysis on the Titanic dataset.  
Explore relationships between variables and identify patterns and trends.

### Dataset
- Source: Titanic dataset (Kaggle)
- Files used: `train.csv`, `test.csv`, `gender_submission.csv`

### Tools Used
- Python (Pandas, Matplotlib, Seaborn)

### Data Cleaning
- Filled missing `Age` values with median.  
- Filled missing `Embarked` values with the most common port.  
- Filled missing `Fare` values with median.  
- Replaced missing `Cabin` values with `"Unknown"`.  

### Visualizations
#### Survival Rate by Gender
![Survival by Gender](outputs/survival_by_gender.png)

#### Survival Rate by Passenger Class
![Survival by Class](outputs/survival_by_class.png)

#### Age Distribution of Passengers
![Age Distribution](outputs/age_distribution.png)

#### Correlation Heatmap
![Correlation Heatmap](outputs/correlation_heatmap.png)

### Insights
- **Gender:** Females had a significantly higher survival rate than males.  
- **Class:** First‑class passengers had better survival chances than third‑class.  
- **Age:** Most passengers were between 20–30 years old; younger passengers had better survival chances.  
- **Correlation:** Fare and class show strong correlation with survival, while age had weaker influence.  

### Conclusion
EDA reveals clear demographic and socio‑economic patterns in Titanic survival rates.  
This highlights the importance of data cleaning and visualization in understanding datasets before modeling.
