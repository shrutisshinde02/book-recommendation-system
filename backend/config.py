import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
TABLE_NAME = os.getenv("TABLE_NAME")

print("DEBUG:", AWS_REGION, TABLE_NAME)  # 👈 add this line temporarily