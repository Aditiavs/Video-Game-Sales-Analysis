# -*- coding: utf-8 -*-
"""capestone_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bcnl6lH0BAHk_lX8bPOO8rQmRCL4f3uQ

## **PHASE 1 - Data Familiarization and Initial Processing**

PROBLEM STATEMENT 1 - ANALYSIS OF ATARI 2600
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('/content/VGsales_datasets.csv')

# Filter for Atari 2600 and years 1980 and 1981
atari_sales = df[(df['Platform'] == '2600') & (df['Year'].isin([1980, 1981]))]

# Group by year and sum sales
atari_sales_trends = atari_sales.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().reset_index()

# Save to a new CSV for Power BI
atari_sales_trends.to_csv('/content/atari_sales_trends.csv', index=False)

#showing the data present in saved CSV file
print(atari_sales_trends)

"""PROBLEM STATEMENT 2 - GENRE PERFORMANCE DASHBOARD"""

# Filter for Atari 2600 and years 1980 and 1981
atari_genres = df[(df['Platform'] == '2600') & (df['Year'].isin([1980, 1981]))]

# Group by genre and sum sales
genre_performance = atari_genres.groupby('Genre')['Global_Sales'].sum().reset_index()

# Save to a new CSV for Power BI
genre_performance.to_csv('/content/atari_genre_performance.csv', index=False)

#printing the first 5 rows of the transformed data
print(genre_performance.head())

"""PROBLEM STATEMENT 3 - REGIONAL GENRE POPULARITY"""

# Group by genre and region (NA, EU)
regional_genre_popularity = atari_genres.groupby(['Genre'])[['NA_Sales', 'EU_Sales']].sum().reset_index()

# Save to a new CSV for Power BI
regional_genre_popularity.to_csv('/content/regional_genre_popularity.csv', index=False)

#printing the first 5 rows of the transformed data
print(regional_genre_popularity.head())

"""## **PHASE 2 - Data Ingestion and Storage Optimization**

PROBLEM STATEMENT 4 - PLATFORM SALES ANALYSIS
"""

x360_sales = df[df['Platform'] == 'X360']

# Sum sales by region for X360
region_sales = x360_sales[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().reset_index()
region_sales.columns = ['Region', 'Total_Sales']

# Save to a new CSV for Power BI
region_sales.to_csv('/content/x360_region_sales.csv', index=False)
print(region_sales.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_x360_region_sales = pd.read_csv('/content/x360_region_sales.csv')
plt.figure(figsize=(10, 6))
sns.barplot(data=df_x360_region_sales, x='Region', y='Total_Sales')
plt.title('X360 Sales in Different Regions')
plt.xticks(rotation=45)
plt.show()

"""PROBLEM STATEMENT 5 - GENRE SPECIFIC SALES IN JAPAN"""

# Filter genres where sales in Japan are higher than in Europe
jp_higher_df = df[df['JP_Sales'] > df['EU_Sales']]

# Save to CSV
jp_higher_df.to_csv('/content/JP_Sales.csv', index=False)

print(jp_higher_df.head())

"""PROBLEM STATEMENT 6 - PS3 SPORTS GAME"""

# Filter for PS3 sports games
ps3_sports_df = df[(df['Platform'] == 'PS3') & (df['Genre'] == 'Sports')]

# Sort by global sales
ps3_sports_sorted_df = ps3_sports_df.sort_values(by='Global_Sales', ascending=False)

# Save to CSV
ps3_sports_sorted_df.to_csv('/content/sportsps.csv', index=False)
print(ps3_sports_sorted_df.head())

"""PROBLEM STATEMENT 7 - POST-2010 SPORTS GAMES ANALYSIS"""

# Check the columns and a few rows to ensure correct loading
print(df.head())
print(df.columns)

# Filter for sports games in action or shooter genres post-2010
post_2010_sports_df = df[(df['Year'] >= 2010) &
                         ((df['Genre'] == 'Action') | (df['Genre'] == 'Shooter'))]

# Check if the filtered DataFrame has values
print(post_2010_sports_df.head())

# Save to CSV
post_2010_sports_df.to_csv('/content/post_2010_sports.csv', index=False)

"""## **PHASE 3 - DATA TRANSFORMATION**

PROBLEM STATEMENT 8 - GENRE RELEASES AND SALES
"""

# Filter for Atari 2600 and years 1980 and 1981
atari_releases_sales = df[(df['Platform'] == '2600') & (df['Year'].isin([1980, 1981]))]

# Group by genre and calculate releases and sales
genre_releases_sales = atari_releases_sales.groupby('Genre').agg({
    'Name': 'count',
    'Global_Sales': 'sum'
}).rename(columns={'Name': 'Releases'}).reset_index()

# Save to a new CSV for Power BI
genre_releases_sales.to_csv('/content/genre_releases_sales.csv', index=False)
print(genre_releases_sales.head())

"""PROBLEM STATEMENT 9 - HIGH SALES GENRE"""

# Filter for specific genres and global sales > 2 million
high_sales_genres = df[(df['Genre'].isin(['Sports', 'Action', 'Shooter'])) &
                       (df['Global_Sales'] > 2) &
                       (~df['Genre'].isin(['Puzzle', 'Fighting', 'Racing']))]

# Save to a new CSV for Power BI
high_sales_genres.to_csv('/content/high_sales_genres.csv', index=False)
print(high_sales_genres.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_high_sales_genres = pd.read_csv('/content/high_sales_genres.csv')

plt.figure(figsize=(10, 6))
sns.barplot(data=df_high_sales_genres, x='Genre', y='Global_Sales')
plt.title('High Sales Genres (Global Sales > 2 million)')
plt.xticks(rotation=45)
plt.show()

"""PROBLEM STATEMENT 10 - DECADE BASED SALES ANALYSIS"""

# Create decade bins
df['Decade'] = pd.cut(df['Year'], bins=[1980, 1990, 2000, 2010, 2017], labels=['1980s', '1990s', '2000s', '2010s'])

# Filter for games sold between 2 million and 10 million
decade_sales = df[(df['Global_Sales'] >= 2) & (df['Global_Sales'] <= 10)]

# Group by decade and genre
decade_genre_sales = decade_sales.groupby(['Decade', 'Genre'])['Global_Sales'].sum().reset_index()

# Save to a new CSV for visualization
decade_genre_sales.to_csv('/content/decade_genre_sales.csv', index=False)
print(decade_genre_sales.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_decade_genre_sales = pd.read_csv('/content/decade_genre_sales.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_decade_genre_sales, x='Decade', y='Global_Sales', hue='Genre')
plt.title('Sales Analysis by Decade')
plt.xticks(rotation=45)
plt.show()

"""## **PHASE 4 - DATA WAREHOUSING AND VISUALIZATION**

PROBLEM STATEMENT 11 - TOP AND UNDERPERFORMING GAMES
"""

# Filter for Atari 2600
atari_games = df[df['Platform'] == '2600']

# Identify top-performing and underperforming games
top_games = atari_games.nlargest(10, 'Global_Sales')
underperforming_games = atari_games.nsmallest(10, 'Global_Sales')

# Combine and save to a new CSV for Power BI
performance = pd.concat([top_games, underperforming_games])
performance.to_csv('/content/atari_performance.csv', index=False)
print(performance.head())

"""PROBLEM STATEMENT 12 - RACING GENRE SALES ANALYSIS"""

# Filter for racing genre and years 2000-2009
racing_sales = df[(df['Genre'] == 'Racing') & (df['Year'].between(2000, 2009))]

# Filter where EU sales are greater than JP, NA, and other sales
eu_dominant_sales = racing_sales[(racing_sales['EU_Sales'] > racing_sales['JP_Sales']) &
                                 (racing_sales['EU_Sales'] > racing_sales['NA_Sales']) &
                                 (racing_sales['EU_Sales'] > racing_sales['Other_Sales'])]

# Get top 5 records for EU sales
top_5_eu_sales = eu_dominant_sales.nlargest(5, 'EU_Sales')[['Name', 'EU_Sales']].set_index('Name')

# Save to a new CSV
top_5_eu_sales.to_csv('/content/racing_eusales.csv')
print(top_5_eu_sales.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_racing_eusales = pd.read_csv('/content/racing_eusales.csv')

plt.figure(figsize=(10, 6))
sns.barplot(data=df_racing_eusales, x='Name', y='EU_Sales')
plt.title('Top 5 EU Sales in Racing Genre (2000-2009)')
plt.xticks(rotation=45)
plt.show()

"""PROBLEM STATEMENT 13 - CUMULATIVE SALES VISUALIZATIONS"""

#PROBLEM STATEMENT 13
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/VGsales_datasets.csv')

# Filter the data for the XB platform
xb_data = df[df['Platform'] == 'XB']

# Group by year and calculate the sum of NA and JP sales
sales_by_year = xb_data.groupby('Year')[['NA_Sales', 'JP_Sales']].sum().reset_index()

# Calculate the cumulative sum of NA sales
sales_by_year['Cumulative_NA_Sales'] = sales_by_year['NA_Sales'].cumsum()

# Plot the cumulative sum of NA sales
plt.figure(figsize=(10, 6))
plt.plot(sales_by_year['Year'], sales_by_year['Cumulative_NA_Sales'], marker='o', linestyle='-')
plt.title('Cumulative NA Sales for XB Platform Over the Years')
plt.xlabel('Year')
plt.ylabel('Cumulative NA Sales')
plt.grid(True)
plt.show()

# Display the aggregated sales data
print(sales_by_year)

"""## **FINAL PHASE - REPORTING AND VISUALIZATION**

PROBLEM STATEMENT 14 - SALES ACRROSS DECADE
"""

# Create decade bins
bins = [1980, 1989, 1999, 2009, 2016]
labels = ['1980s', '1990s', '2000s', '2010s']
df['Decade'] = pd.cut(df['Year'], bins=bins, labels=labels, right=True)

# Group by decade and region
decade_sales_region = df.groupby(['Decade']).agg({
    'NA_Sales': 'sum',
    'EU_Sales': 'sum',
    'JP_Sales': 'sum',
    'Other_Sales': 'sum',
    'Global_Sales': 'sum'
}).reset_index()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_decade_sales_region = pd.read_csv('/content/decade_sales_region.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_decade_sales_region, x='Decade', y='Global_Sales')
plt.title('Global Sales Across Decades')
plt.show()

# Save to a new CSV
decade_sales_region.to_csv('/content/decade_sales_region.csv', index=False)
print(decade_sales_region.head())

"""PROBLEM STATEMENT 15 - FEATURE IMPACT ON SALES"""

# Filter for Atari 2600 platform
atari_games = df[df['Platform'] == '2600']

# Group by genre and publisher to analyze their impact on sales
feature_impact = atari_games.groupby(['Genre', 'Publisher']).agg({
    'Global_Sales': 'sum'
}).reset_index()

# Save to a new CSV
feature_impact.to_csv('/content/feature_impact.csv', index=False)
print(feature_impact.head())

df_feature_impact = pd.read_csv('/content/feature_impact.csv')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(data=df_feature_impact, x='Genre', y='Global_Sales')
plt.title('Impact of Genre on Sales for Atari 2600')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_feature_impact, x='Publisher', y='Global_Sales')
plt.title('Impact of Publisher on Sales for Atari 2600')
plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed data
df_platform_sales = pd.read_csv('/content/atari_genre_performance.csv')
df_genre_sales = pd.read_csv('/content/regional_genre_popularity.csv')
df_x360_region_sales = pd.read_csv('/content/x360_region_sales.csv')
df_genre_releases_sales = pd.read_csv('/content/genre_releases_sales.csv')
df_high_sales_genres = pd.read_csv('/content/high_sales_genres.csv')
df_decade_genre_sales = pd.read_csv('/content/decade_genre_sales.csv')
df_atari_performance = pd.read_csv('/content/atari_performance.csv')
df_racing_eusales = pd.read_csv('/content/racing_eusales.csv')
df_xb_cumulative_sales = pd.read_csv('/content/xb_cumulative_sales.csv')
df_decade_sales_region = pd.read_csv('/content/decade_sales_region.csv')
df_feature_impact = pd.read_csv('/content/feature_impact.csv')

# Visualization examples

# Problem 2: Platform Popularity (2006-2008)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_platform_sales, x='Genre', y='Global_Sales')
plt.title('Platform Popularity (2006-2008)')
plt.xticks(rotation=45)
plt.show()

# Problem 3: Genre Popularity
plt.figure(figsize=(10, 6))
sns.barplot(data=df_genre_sales, x='Genre', y='NA_Sales')
plt.title('Genre Popularity')
plt.xticks(rotation=45)
plt.show()

# Problem 4: X360 Popularity in Different Countries
plt.figure(figsize=(10, 6))
sns.barplot(data=df_x360_region_sales, x='Region', y='Total_Sales')
plt.title('X360 Sales in Different Regions')
plt.xticks(rotation=45)
plt.show()

# Problem 8: Genre Releases and Sales (1980-1981)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_genre_releases_sales, x='Genre', y='Releases')
plt.title('Genre Releases (1980-1981)')
plt.xticks(rotation=45)
plt.show()

# Problem 9: High Sales Genres (Global Sales > 2 million)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_high_sales_genres, x='Genre', y='Global_Sales')
plt.title('High Sales Genres (Global Sales > 2 million)')
plt.xticks(rotation=45)
plt.show()

# Problem 10: Decade-Based Sales Analysis
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_decade_genre_sales, x='Decade', y='Global_Sales', hue='Genre')
plt.title('Sales Analysis by Decade')
plt.xticks(rotation=45)
plt.show()

# Problem 11: Top and Underperforming Games on Atari 2600
plt.figure(figsize=(10, 6))
sns.barplot(data=df_atari_performance, x='Name', y='Global_Sales')
plt.title('Top and Underperforming Games on Atari 2600')
plt.xticks(rotation=45)
plt.show()

# Problem 12: Racing Genre Sales Analysis (2000-2009)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_racing_eusales, x='Name', y='EU_Sales')
plt.title('Top 5 EU Sales in Racing Genre (2000-2009)')
plt.xticks(rotation=45)
plt.show()

# Problem 13: Cumulative Sales Visualization for XB Platform
plt.figure(figsize=(20, 6))
plt.plot(df_xb_cumulative_sales['Name'], df_xb_cumulative_sales['Cumulative_NA_Sales'], label='NA Sales')
plt.plot(df_xb_cumulative_sales['Name'], df_xb_cumulative_sales['Cumulative_JP_Sales'], label='JP Sales')
plt.title('Cumulative Sales for XB Platform')
plt.xlabel('Games')
plt.ylabel('Cumulative Sales')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Problem 14: Sales Across Decades
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_decade_sales_region, x='Decade', y='Global_Sales')
plt.title('Global Sales Across Decades')
plt.show()

# Problem 15: Feature Impact on Sales
plt.figure(figsize=(10, 6))
sns.barplot(data=df_feature_impact, x='Genre', y='Global_Sales')
plt.title('Impact of Genre on Sales for Atari 2600')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_feature_impact, x='Publisher', y='Global_Sales')
plt.title('Impact of Publisher on Sales for Atari 2600')
plt.xticks(rotation=45)
plt.show()

"""PHASE 2 ALTERNATIVE"""

import pandas as pd

# Load the dataset
df = pd.read_csv('/content/VGsales_datasets.csv')

# Display basic information and first few rows
print(df.info())
print(df.head())

#ps 4
# Extract records for X360 platform
x360_sales = df[df['Platform'] == 'X360']

# Summarize sales by region
x360_region_sales = x360_sales[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()

# Save results
x360_sales.to_csv('/content/x360_sales.csv', index=False)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
sales_values = x360_region_sales[regions].values

plt.figure(figsize=(10, 6))
sns.barplot(x=regions, y=sales_values)
plt.title('X360 Sales in Different Regions')
plt.xlabel('Region')
plt.ylabel('Total Sales (millions)')
plt.show()

#ps 5
# Extract records where sales in Japan were higher than in Europe
jp_higher_sales = df[df['JP_Sales'] > df['EU_Sales']]

# Save the records to a CSV file
jp_higher_sales.to_csv('/content/JP_Sales.csv', index=False)

# Analyze the contribution of different genres
genre_sales_jp = jp_higher_sales.groupby('Genre').agg({
    'JP_Sales': 'sum',
    'NA_Sales': 'sum',
    'EU_Sales': 'sum',
    'Other_Sales': 'sum',
    'Global_Sales': 'sum'
}).reset_index()

# Visualization
plt.figure(figsize=(12, 8))
sns.barplot(data=genre_sales_jp.melt(id_vars='Genre', value_vars=['JP_Sales', 'NA_Sales', 'EU_Sales', 'Other_Sales']), x='Genre', y='value', hue='variable')
plt.title('Genre-Specific Sales Contribution in Various Regions')
plt.xticks(rotation=45)
plt.show()

#PS 6
# Extract records for PS3 sports games and sort by global sales
ps3_sports = df[(df['Platform'] == 'PS3') & (df['Genre'] == 'Sports')].sort_values(by='Global_Sales', ascending=False)

# Save the records to a CSV file
ps3_sports.to_csv('/content/sportsps.csv', index=False)

#PS 7
# Extract records for sports games in action or shooter genres since 2010
sports_post_2010 = df[(df['Year'] >= 2010) & (df['Genre'].isin(['Action', 'Shooter']))]

# Save the records to a CSV file
sports_post_2010.to_csv('/content/sports_post_2010.csv', index=False)

# Visualize the distribution of global sales
plt.figure(figsize=(10, 6))
sns.histplot(sports_post_2010['Global_Sales'], kde=True)
plt.title('Distribution of Global Sales for Post-2010 Sports Games')
plt.xlabel('Global Sales (millions)')
plt.ylabel('Frequency')
plt.show()

import sqlite3
# Change the database path to the correct SQLite database file
conn = sqlite3.connect('/content/vgsales.db')

# Create table and load cleaned data
df.to_sql('vgsales', conn, if_exists='replace', index=False)

#/* ps 4 */
#SELECT * FROM vgsales WHERE Platform = 'X360';

#/* ps 5 */
#SELECT * FROM vgsales WHERE JP_Sales > EU_Sales;

#/* ps 6 */
#SELECT * FROM vgsales WHERE Platform = 'PS3' AND Genre = 'Sports' ORDER BY Global_Sales DESC;

#/* ps 7*/
#SELECT * FROM vgsales WHERE Year >= 2010 AND Genre IN ('Action', 'Shooter');

#PROBLEM STATEMENT 13
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
# Assuming the CSV file is named '/content/VGsales_datasets.csv' and has columns 'Platform', 'Year', 'NA_Sales', 'JP_Sales'
df = pd.read_csv('/content/VGsales_datasets.csv')

# Filter the data for the XB platform
xb_data = df[df['Platform'] == 'XB']

# Group by year and calculate the sum of NA and JP sales
sales_by_year = xb_data.groupby('Year')[['NA_Sales', 'JP_Sales']].sum().reset_index()

# Calculate the cumulative sum of NA sales
sales_by_year['Cumulative_NA_Sales'] = sales_by_year['NA_Sales'].cumsum()

# Plot the cumulative sum of NA sales
plt.figure(figsize=(10, 6))
plt.plot(sales_by_year['Year'], sales_by_year['Cumulative_NA_Sales'], marker='o', linestyle='-')
plt.title('Cumulative NA Sales for XB Platform Over the Years')
plt.xlabel('Year')
plt.ylabel('Cumulative NA Sales')
plt.grid(True)
plt.show()

# Display the aggregated sales data
print(sales_by_year)
