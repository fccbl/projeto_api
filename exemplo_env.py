import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")

print(f"o token é {token}")