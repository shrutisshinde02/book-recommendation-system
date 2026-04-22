import streamlit as st
import requests

# 🔗 Your API URL
API_URL = "https://si88npoere.execute-api.ap-south-1.amazonaws.com/prod/recommend"

# Book images
book_images = {
    "The Silent Patient": "https://images-na.ssl-images-amazon.com/images/I/81JJPDNlxSL.jpg",
    "Gone Girl": "https://images-na.ssl-images-amazon.com/images/I/71+1k2B2YcL.jpg",
    "The Hobbit": "https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
}

# Page config
st.set_page_config(page_title="Book Recommender", layout="centered")

# 🌗 Dark / Light toggle
mode = st.toggle("🌙 Dark Mode")

# 🎨 Theme colors
if mode:
    bg_color = "#0e1117"
else:
    bg_color = "#e6f2ff"  # pastel blue

# Apply background
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📚 Book Recommendation System")
st.write("Find your next favorite book easily!")

# 🎯 Dropdown
genre_option = st.selectbox(
    "Select a genre",
    ["", "thriller", "fantasy", "self-help", "romance"]
)

# Suggestions
suggestions = ["thriller", "fantasy", "romance", "self-help", "mystery"]

# Input
user_input = st.text_input("Search books")

# Suggestions display
if user_input:
    filtered = [s for s in suggestions if user_input.lower() in s]

    if filtered:
        st.write("Suggestions:")
        cols = st.columns(len(filtered))
        for i, s in enumerate(filtered):
            if cols[i].button(s):
                user_input = s

# Final input
final_input = user_input if user_input else genre_option

# Button
if st.button("Get Recommendations"):
    if final_input:
        response = requests.post(API_URL, json={"preferences": final_input})

        if response.status_code == 200:
            books = response.json()

            if books:
                st.subheader("📖 Recommended Books")

                for book in books:
                    with st.container():
                        col1, col2 = st.columns([1, 3])

                        with col1:
                            image_url = book_images.get(book['title'], "")
                            if image_url:
                                st.image(image_url, width=120)

                        with col2:
                            st.markdown(f"### {book['title']}")
                            st.write(f"**Genre:** {book['genre']}")
                            st.write(book['summary'])

                        st.markdown("---")

            else:
                st.warning("No recommendations found 😔")
        else:
            st.error("API Error ❌")
    else:
        st.warning("Please select or enter something!")