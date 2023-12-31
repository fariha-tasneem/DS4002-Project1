# DS 4002 Project 1

## Table of Contents
[SRC](#SRC)  - This section contains all the source code for our project, which includes cleaning.ipynb, where we cleaned the original dataset from Kaggle and also completed our initial exploratory data analysis, as well as analysis.ipynb, which contains the main analysis of our project.

[DATA](#Data)  - This section contains "top_30_genres.csv". This is the dataset used to run analysis.ipynb.

[FIGURES](#Figures)  - This section contains all figures from our main analysis phase, as well as descriptions of their key takeaways.

[References](#References)  - This section contains all references that were used throughout the project, as well as links to the MI1 and MI2 Assignments.

## SRC

### Installing/Building Code
To install/build the code, VSCode and the Jupyter Notebook extension or Jupyter Notebook is required. Then, the script and dataset is required to run the code. Ensure the correct directory is specified for the dataset before running the code. 

Required libraries:
- pandas
- textblob
- matplotlib
- wordcloud

For cleaning.ipynb, we used the datasets from Kaggle to establish our project dataset. This entails dropping rows with missing values, specifying which columns we wanted to keep, etc. Then, we were able to write the cleaned up dataframe to a CSV file called "top_30_genres.csv" (this file is in the "Data" folder in this repository). cleaning.ipynb also contains our initial exploratory data analysis. In analysis.ipynb, we used the "top_30_genres.csv" file to conduct our main analysis to investigate our hypothesis.

### Usage of Code
The code can be used to replicate our analysis or build upon it.

## DATA

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

## FIGURES

### Figures Table
| Column| Description| Plot Type|                   
|-------|------------|-------------------|
| Figure 1 | This is a boxplot that shows the sentiment scores of the 30 genres with the most number of reviews. Using the libraries seaborn and matplotlib.pyplot, we created this boxplot where the x-axis is the categories and the y-axis the the sentiment score. This sentiment score was assigned to each genre using a built in function called analysis.sentiment.polarity in the TextBlob library. This graph clearly highlights the fact that all of these genre's sentiment scores are similar as they all lie around 0.25. This is means that on average, most genres have reviews with slightly positive sentiments. | Box Plot|
| Figure 2 | This is a barplot that shows the sentiment score of each of the 30 genres with the largest number of reviews. Using the libraries seaborn and matplotlib.pyplot, we created this boxplot where the x-axis is the categories and the y-axis the the sentiment score. This sentiment score was assigned to each genre using a built in function called analysis.sentiment.polarity in the TextBlob library. For this plot, we decreased the range of the y-axis so we would be able to see more variation within the sentiment. It is clear that juvenile nonfiction, cooking, crafts and hobbies, and education have the highest rating for sentiment score which means they are probably the most well-liked genres. Still, though, there is not much variation between the genres as all of their sentiment scores lie right around 0.25. | Bar Plot |



## REFERENCES 
[1] "Amazon Books Reviews" Dataset, Kaggle. [Online]. Available: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?select=Books_rating.csv. [Accessed: 09-Sep-2023]

[2] E.-R. Luţan and C. Bădică, "Emotion-Based Literature Book Classification Using Online Reviews," Electronics, vol. 11, p. 3412, 2022. [Online]. Available: https://doi.org/10.3390/electronics11203412. [Accessed: 09-Sep-2023].

[3] "Poll Shows Continuing Strong American Reading Habits," Gallup, [Online]. Available: https://news.gallup.com/poll/3562/poll-shows-continuing-strong-american-reading-habits.aspx. [Accessed: 09-Sep-2023]. 

[4] T. A. Team, “Sentiment analysis with logistic regression,” Towards AI, https://towardsai.net/p/nlp/sentiment-analysis-with-logistic-regression [Accessed: 10-Sep-2023]. 

### MI1 and MI2 Assignments
MI1 Assigment: https://docs.google.com/document/d/1gfmBZ31x9V9vEbQJCZwRirUR76DM6iHGpRKLZxJ86ek/edit?usp=sharing

MI2 Assignment: https://docs.google.com/document/d/10TgF1NxPdTjxaYZGttimPwlkUSGeDwzdhq_BBxlI6IM/edit?usp=sharing
