import json
import os
from backend.dynamodb_utils import get_all_books
from backend.comprehend_utils import extract_keywords

def load_books():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "books.json")

    with open(file_path, "r") as f:
        return json.load(f)

def get_recommendations(user_input):
    books = get_all_books()
    user_input = user_input.lower()

    keywords = extract_keywords(user_input)
    print("Extracted keywords:", keywords)

    matched_books = []

    for book in books:
        genre = book.get("genre", "").lower()
        summary = book.get("summary", "").lower()

        if any(keyword in genre or keyword in summary for keyword in keywords):
            matched_books.append(book)

    return matched_books[:5]