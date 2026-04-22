import os

AWS_REGION = os.environ.get("AWS_REGION")   # Lambda gives this automatically
TABLE_NAME = os.environ.get("TABLE_NAME")