import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.recommender import get_recommendations

user_input = "I like mystery and thriller books"

result = get_recommendations(user_input)

print(result)