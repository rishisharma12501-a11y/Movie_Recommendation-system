🎬 Movie Recommendation System
A high-performance Python-based recommendation engine that suggests movies based on genre similarity using Natural Language Processing (NLP).

🚀 Features

Content-Based Filtering: Recommends movies by analyzing metadata patterns.

NLP Powered: 

Utilizes TF-IDF Vectorization to convert text data into meaningful mathematical vectors.


Similarity Scoring: Uses Cosine Similarity to calculate the distance between movie profiles.
Excel Integration: Seamlessly handles .xlsx databases using Pandas.


🛠️ Tech Stack

Language: Python 3.x
Data Handling: Pandas, OpenPyXL
Machine Learning: Scikit-Learn (TF-IDF, Cosine Similarity)


📂 Project Structure
├── data/
│   └── movie.xlsx         # The movie database
├── scripts/
│   └── main.py            # Main application logic
├── requirements.txt       # Necessary libraries
└── README.md

⚙️ Installation & Setup

git clone https://github.com/rishisharma12501-a11y/Movie_Recommendation-system

cd Movie_Recommendation-system
add movies.xlsv in same folder/directory
📊 How it Works
The system follows a mathematical approach to find the "closest" movie to your input:
Preprocessing: Cleans the Genre data from the Excel sheet.
Vectorization: Converts genres into a matrix of TF-IDF features.
Similarity: Calculates the Cosine \theta between vectors.
Ranking: Returns the top 5 movies with the highest similarity scores.

One more thing you need:
Before you upload, you should create a file named requirements.txt in your folder and paste these three lines inside it:


pandas
openpyxl
scikit-learn

CRUCIAL NOTE : add movies.xlsv in a same directory as Movie_Recommandation.py
