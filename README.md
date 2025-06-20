# 🎬 Movie Recommender System — Content-Based

A content-based movie recommender system built with Python and Streamlit that recommends movies based on similarity in content metadata such as genres, keywords, cast, and overview.

---

## 🚀 Features

- 📽️ Movie recommendations using cosine similarity
- 🧠 Content-based filtering with vectorized metadata
- 🎯 TMDB API integration for movie posters (via hardcoded ID for now)
- ⚙️ Interactive Streamlit interface
- 📊 Precomputed similarity matrix for fast results

---

## 📦 Project Structure

movie-recommender/
├── app.py # Streamlit frontend
├── movies.pkl # Movie metadata DataFrame
├── new_df.pkl # Cleaned and merged dataset
├── similarity.pkl # Precomputed cosine similarity matrix
├── vectorizer.pkl # Fitted CountVectorizer or TfidfVectorizer
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── LICENSE # MIT License

---

## 🛠️ Setup Instructions

### ▶️ Run Locally

```bash
git clone https://github.com/SREENATH-065/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
```
Create a .env file in the root directory:
```bash
TMDB_API_KEY=your_tmdb_api_key
```
Then start the app:
```bash
streamlit run app.py
```
##🧪 How It Works

The movies.pkl and new_df.pkl files store the movie dataset.

Vectorizer encodes content metadata into numerical vectors.

Cosine similarity is used to find and rank similar movies.

Movie posters are fetched from TMDB using hardcoded movie IDs (for now).

🛠️ Note: TMDB ID is currently hardcoded for demo purposes. This will be dynamically fetched in the upcoming version.

##📌 Roadmap

✅ Initial version with hardcoded TMDB ID

🔜 Dynamic TMDB search based on movie title

🔜 Add filtering by rating, genre, release year

🔜 Improve UI with poster grid display

##✅ Use Cases

📚 Learn the fundamentals of content-based recommendation systems

🧠 Understand vectorization and cosine similarity

🎥 Get instant movie suggestions by title

🔄 Base project for hybrid recommender systems

##📜 License

MIT License © 2025 SREENATH S

