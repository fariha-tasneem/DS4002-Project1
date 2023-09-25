# SRC

### Installing/Building Code
To install/build the code, VSCode and the Jupyter Notebook extension or Jupyter Notebook is required. Then, the script and dataset is required to run the code. Ensure the correct directory is specified for the dataset before running the code. 

Required libraries:
- pandas
- textblob
- matplotlib
- wordcloud
- textblob

### Usage of Code
The code can be used to replicate our analysis or build upon it.

# DATA

### Link to Dataset
[See file](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews)

### Data Dictionary
| Column| Description| Potential Reponses|                   
|-------|------------|-------------------|
| Title | The book's title | string format|
| Description | A description of the book | Can be a basic summary of the book/provide details for the book |
| Author | Name(s) of the book author(s) | i.e. "Veronica Haddon" |
| Publisher | Name of the book publisher | i.e. "iUniverse" |
| publishedDate | The date the book was published | i.e. "2020-08-06" |
| Category/Genre | The genre(s) of the book | i.e "Fiction" or "Nonfiction"|
| User_id| Provides the ID of the user who provided the rating| a sequence of letters and numbers |
| profileName| Profile name of the user who provided the book rating | i.e. "John Doe" |
| review/helpfulness| Helpfulness rating of review | i.e. "7/7" or "74/81" |
| review/score| Rating from 0 to 5 for the book | i.e. "4" or "2" |
| review/text| The full text of an amazon book review | i.e. "This book was really good." |

# FIGURES

### Figures Table
| Column| Description| Plot Type|                   
|-------|------------|-------------------|
| Figure 1 | This is a boxplot that shows the sentiment scores of the 30 genres with the most number of reviews. Using the libraries seaborn and matplotlib.pyplot, we created this boxplot where the x-axis is the categories and the y-axis the the sentiment score. This sentiment score was assigned to each genre using a built in function called analysis.sentiment.polarity in the TextBlob library. This graph clearly highlights the fact that all of these genre's sentiment scores are similar as they all lie around 0.25. This is means that on average, most genres have reviews with slightly positive sentiments. | Box Plot|
| Figure 2 | This is a barplot that shows the sentiment score of each of the 30 genres with the largest number of reviews. Using the libraries seaborn and matplotlib.pyplot, we created this boxplot where the x-axis is the categories and the y-axis the the sentiment score. This sentiment score was assigned to each genre using a built in function called analysis.sentiment.polarity in the TextBlob library. For this plot, we decreased the range of the y-axis so we would be able to see more variation within the sentiment. It is clear that juvenile nonfiction, cooking, crafts and hobbies, and education have the highest rating for sentiment score which means they are probably the most well-liked genres. Still, though, there is not much variation between the genres as all of their sentiment scores lie right around 0.25. | Bar Plot |



# REFERENCES
