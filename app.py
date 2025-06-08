import streamlit as st
import pickle
import requests


# Load data
new_df = pickle.load(open('new_df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

import time
import requests

def fetch_poster(id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{id}?api_key=57a59cfbc1283b4045b18d44d1ed7fa7&language=en-US'
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for ID {id}: {e}")
        return "https://via.placeholder.com/500x750.png?text=Poster+Not+Available"


# Recommend function
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    recommended_poster=[]
    for i in movies_list:
        title = new_df['title'][i[0]]
        year = new_df['release_date'][i[0]]
        id=new_df['id'][i[0]]
  #fetch poster
        recommended_poster.append(fetch_poster(id))
        recommendations.append(f"{title} ({year})")

    return recommendations,recommended_poster


# UI
st.title("🎬 Movie Recommender")

options = [f"{t} ({y})" for t, y in zip(new_df['title'], new_df['release_date'])]
selected_display = st.selectbox("Select a movie", options)
selected_movie = selected_display.split(' (')[0]  # Get title before " ("




if st.button("Recommend"):
    name,poster = recommend(selected_movie)
    st.write("### Recommended Movies:")
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(5):
        with [col1, col2, col3, col4, col5][i]:
            st.image(poster[i])
            st.caption(name[i])
