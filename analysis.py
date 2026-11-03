# import pandas for loading, cleaning, and analyzing tabular data
import pandas as pd

# import NumPy for working with missing values and numeric ops
import numpy as np

# import matplotlib for charts and visualizations
import matplotlib.pyplot as plt

# ==========================================================
# Load and inspect the cervical cancer risk factors dataset
# ==========================================================

# load the cervical cancer risk factor dataset from the CSV file & store in pandas dataframe
df = pd.read_csv("risk_factors_cervical_cancer.csv")
# display the first five rows to verify the data loaded correctly
print(df.head())
# display all column names to identify available variables
print(df.columns)
# display the number of rows and columns in the dataset
print(df.shape)
# display variable data types and basic dataset information
print(df.info())

# ==========================================================
# Data cleaning and missing value assessment
# ==========================================================

# replace all "?" entries with NaN (Not a Number), using pandas to recognize as a missing value
df.replace("?", np.nan, inplace=True)
# count the number of missing values in each variable to identify data quality issues before analysis
print(df.isnull().sum())

# =================================================================================
# Research Question 1:
# What percentage of women in the dataset had a positive cervical biopsy result?
# =================================================================================

# calculate the proportion of participants with a positive biopsy
# (Biopsy is coded as 0 = negative, 1 = positive)
biopsy_rate = df["Biopsy"].mean()

# display the biopsy positivity rate as a proportion
print("Biopsy positivity rate:", biopsy_rate)
# display as a percent
print("Biopsy positivity percent:", biopsy_rate * 100)

# create a bar chart showing the distribution of biopsy results
df["Biopsy"].value_counts().plot(kind="bar")

# add chart labels and titles
plt.title("Biopsy Results")
plt.xlabel("Biopsy")
plt.ylabel("Count")
# save the figure for inclusion in the project report and poster
plt.savefig("biopsy_results.png")
# close the figure to prepare for the next visualization
plt.close()


# =================================================================================
# Research Question 2:
# What is the age distribution of women with a positive cervical biopsy result?
# =================================================================================

# create a subset containing only women with positive biopsy findings
biopsy_positive = df[df["Biopsy"] == 1]

# calculate descriptive statistics for age among biopsy-positive women
print("Mean age:", biopsy_positive["Age"].mean())
print("Median age:", biopsy_positive["Age"].median())
print("Minimum age:", biopsy_positive["Age"].min())
print("Maximum age:", biopsy_positive["Age"].max())

# create a histogram to visualize the age distribution of women with positive biopsy results
plt.hist(biopsy_positive["Age"])
# add chart labels and titles
plt.title("Age Distribution of Biopsy Positive Women")
plt.xlabel("Age")
plt.ylabel("Count")
# save the figure for inclusion in the project report and poster
plt.savefig("age_dist_results.png")
# close the figure to prepare for the next visualization
plt.close()

# ============================================================
# create a new variable for age group for subgroup analysis
# ============================================================

# categorize participants into age groups to compare biopsy positivity across different age ranges
df["Age_Group"] = pd.cut(
    df["Age"], bins=[0, 24, 34, 100], labels=["<25", "25-34", "35+"]
)
# display number of positive and negative biopsy results in each age group
print(pd.crosstab(df["Age_Group"], df["Biopsy"]))

# ==========================================================
# Examine biopsy positivity rates by age group
# ==========================================================

# calculate the percent positive biopsy results in each age group
age_table = pd.crosstab(df["Age_Group"], df["Biopsy"], normalize="index") * 100

# create a bar chart showing biopsy positivity percentages across age groups
age_table[1].plot(kind="bar")
# add chart labels and titles
plt.title("Biopsy Positivity by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Percent Positive")
# save the figure for inclusion in the project report and poster
plt.savefig("age_group_results.png")
# close the figure to prepare for the next visualization
plt.close()


# =================================================================================
# Research Question 3:
# Is hormonal contraceptive use associated with positive cervical biopsy findings?
# =================================================================================

# -------------------------------------------------------------------------------
# Create a dataset with complete contraceptive information
# Missing values are excluded for contraceptive analyses
# -------------------------------------------------------------------------------

contraceptive_df = df.dropna(subset=["Hormonal Contraceptives"])


# convert hormonal contraceptive use variable from string to numeric format
contraceptive_df["Hormonal Contraceptives"] = pd.to_numeric(
    df["Hormonal Contraceptives"], errors="coerce"
)

# display the frequency distribution of biopsy results stratified by hormonal contraceptive use
print(
    pd.crosstab(contraceptive_df["Hormonal Contraceptives"], contraceptive_df["Biopsy"])
)

# create a bar chart showing the number of positive and negative biopsy results among contraceptive users and non-users
pd.crosstab(
    contraceptive_df["Hormonal Contraceptives"], contraceptive_df["Biopsy"]
).plot(kind="bar")
# add chart labels and titles
plt.title("Biopsy Results by Hormonal Contraceptive Use")
plt.xlabel("Hormonal Contraceptive Use")
plt.ylabel("Count")
# save the figure for inclusion in the project report and poster
plt.savefig("contraception_results_count.png")
# close the figure to prepare for the next visualization
plt.close()

# -------------------------------------------------------------------------------
# calculate biopsy positivity percentages
# -------------------------------------------------------------------------------

# calculate the percentage of positive biopsy results within each contraceptive-use group
contraceptive_table = (
    pd.crosstab(
        contraceptive_df["Hormonal Contraceptives"],
        contraceptive_df["Biopsy"],
        normalize="index",
    )
    * 100
)
# display biopsy positivity percentages for contraceptive users and non-users
print(contraceptive_table)

# create a bar chart showing the percentage of women with positive biopsy results in each contraceptive-use group
contraceptive_table[1].plot(kind="bar")

# add chart labels and titles
plt.title("Biopsy Results by Hormonal Contraceptive Use")
plt.xlabel("Hormonal Contraceptive Use")
plt.ylabel("Percent positive")
# save the figure for inclusion in the project report and poster
plt.savefig("contraception_results_percent.png")
# close the figure to prepare for the next visualization
plt.close()
