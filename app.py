import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Anime Recommendation System",
    page_icon="🎬"
)

anime_df = pickle.load(
    open("anime_list.pkl", "rb")
)

similarity = pickle.load(
    open("similarity.pkl", "rb")
)

st.title("🎬 Anime Recommendation System")

st.write(
    "Select an anime and get similar recommendations."
)

selected_anime = st.selectbox(
    "Choose Anime",
    anime_df["name"].values
)

def recommend_anime(anime_name):

    anime_index = anime_df[
        anime_df["name"] == anime_name
    ].index[0]

    similarity_scores = list(
        enumerate(similarity[anime_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:6]

    recommendations = []

    for item in similarity_scores:
        recommendations.append(
            anime_df.iloc[item[0]]["name"]
        )

    return recommendations

if st.button("Get Recommendations"):

    results = recommend_anime(
        selected_anime
    )

    st.subheader(
        "Recommended Anime"
    )

    for anime in results:
        st.write("✅", anime)