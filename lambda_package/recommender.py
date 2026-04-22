from dynamodb_utils import get_all_books

def get_recommendations(user_input):
    books = get_all_books()
    user_words = user_input.lower().split()

     # ✅ ADD THESE LINES HERE
    print("BOOKS:", books)
    print("INPUT:", user_words)

    scored_books = []

    for book in books:
        score = 0

        genre = book.get("genre", "").lower()
        summary = book.get("summary", "").lower()

        for word in user_words:
            if word in genre:
                score += 3   # higher weight for genre match
            if word in summary:
                score += 1

        if score > 0:
            scored_books.append((score, book))

    # sort books by score (highest first)
    scored_books.sort(reverse=True, key=lambda x: x[0])

    # return only book data (top 5)
    return [book for score, book in scored_books[:5]]
