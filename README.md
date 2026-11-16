Cervical Cancer Risk Factors Analysis

Author: Daryn Smith

Research Questions
What proportion of women had a positive biopsy result?
What is the age distribution among women with positive biopsy findings?
Is hormonal contraceptive use associated with positive biopsy findings?

Data Source:
Data were obtained from the Cervical Cancer (Risk Factors) dataset available through the UCI Machine Learning Repository.
The dataset contains demographic, reproductive, behavioral, and clinical variables associated with cervical cancer screening outcomes among 858 women. The primary outcome variable for this study was biopsy result, which was coded as 0 (negative) or 1 (positive). Data were analyzed using Python with the Pandas, NumPy, and Matplotlib libraries.

Methods
pre-processed data to recode missing values and created new variable for age categories
Descriptive statistics were calculated for age among participants with positive biopsy findings, including mean, median, minimum, and maximum age.
Frequency distributions and cross-tabulations were used to evaluate biopsy prevalence overall and within age groups and hormonal contraceptive-use groups.

Visualizations included:
Pie chart of biopsy prevalence
Bar chart of biopsy positivity by age group
Histogram of age among biopsy-positive participants
100% stacked bar chart of biopsy positivity by age group (percents)
Bar chart of biopsy positivity by hormonal contraceptive use (counts)


Main Findings
6.4% of women had a positive biopsy result.
Women 35 years and older had the highest biopsy positivity rate.
Hormonal contraceptive users had a biopsy positivity rate of 7.48%, compared to 7.06% among non-users.

Files
analysis.py
risk_factors_cervical_cancer.csv
biopsy_results.png
age_dist_results.png
age_group_results.png
contraception_results_count.png
contraception_results_percent.png