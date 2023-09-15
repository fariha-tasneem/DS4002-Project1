import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('/Users/farihatasneem/Downloads/Books_rating.csv')
# Read the second CSV file (replace 'second_csv.csv' with the actual filename)
df2 = pd.read_csv('/Users/farihatasneem/Downloads/books_data.csv')

columns_to_combine = ['description', 'authors', 'publisher', 'publishedDate', 'categories', 'ratingsCount'] 
common_column = 'Title'
combined_df = df1.merge(df2[columns_to_combine], on=common_column, how='inner')
