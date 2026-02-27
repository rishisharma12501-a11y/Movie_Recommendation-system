import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, file_path):
        try:
            print("⏳ Data load ho raha hai...")
            # Excel file read karne ke liye
            self.df = pd.read_excel(file_path)
            
            # Column names clean karein
            self.df.columns = self.df.columns.str.strip()
            
            # Zaroori columns check karein
            if 'Title' not in self.df.columns or 'Genre' not in self.df.columns:
                raise ValueError("In File 'Title' or 'Genre' column not Found!")

            self.prepare_data()
            print("✅ System is ready..Movie DETECTIVE🎧😎😎")
            
        except Exception as e:
            print(f"❌ Error: {e}")

    def prepare_data(self):
        # Missing values handle karein
        self.df['Genre'] = self.df['Genre'].fillna('')

        # Vectorization (Genre words ko numbers mein badalna)
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['Genre'])
        
        # Similarity matrix calculate karein
        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Titles ka index map
        self.indices = pd.Series(self.df.index, index=self.df['Title'].str.lower().str.strip()).drop_duplicates()

    def recommend(self, movie_title):
        search_title = movie_title.lower().strip()
        
        if search_title not in self.indices:
            return None
        
        idx = self.indices[search_title]
        
        if isinstance(idx, pd.Series):
            idx = idx.iloc[0]

        # Scores nikal kar sort karein
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Top 5 movies dikhayein
        movie_indices = [i[0] for i in sim_scores[1:6]]
        return self.df.iloc[movie_indices][['Title', 'Genre']]

# --- Main Program ---
if __name__ == "__main__":
    # Make sure your file name is movie.xlsx
    recommender = MovieRecommender("movies.xlsx")

#Hollywood (mostly) Database
    while True:
        movie_name = input("\n🎬 Enter Movie Name : ").strip()
        
        if movie_name.lower() == 'exit':
            break
            
        recommendations = recommender.recommend(movie_name)
        
        if recommendations is not None:
            print(f"\n🌟 Similar Movies for '{movie_name}':")
            print("-" * 40)
            for i, row in enumerate(recommendations.itertuples(), 1):
                print(f"{i}. {row.Title} (Genre: {row.Genre})")
            print("-" * 40)
        else:
            print("\n⚠️  Movie not Found ,Check for grammatical mistake or Database still need to be updated>>>>.")
