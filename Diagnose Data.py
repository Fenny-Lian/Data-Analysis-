# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())

# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())

#Frequency counts:continent
df.continent.value_counts(dropna = False)
df.country.value_counts(dropna = False).head()
df['spot outliy'].value_counts(dropna = False)
df.describe()

#Data visualization is great way to spot outliers and obvious errors
#Bar plots for discrete data counts Histograms for continuous data counts

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Describe the column
df['Existing Zoning Sqft'].describe()

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

#Identifying the error
df[df.population > 10000]
#Not all outliers are bad data points
#some can be an error, but others are valid values

#Box plot
df.boxplot(column='population', by='continent')
plt.show()

#scatter plots
#Relationship between 2 numeric variables
#flag potentially bad data
