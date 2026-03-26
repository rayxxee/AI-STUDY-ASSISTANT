import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    with open("models.txt", "w") as f:
        for m in genai.list_models():
            if 'embedContent' in m.supported_generation_methods:
                f.write(m.name + "\n")
except Exception as e:
    with open("models.txt", "w") as f:
        f.write(str(e))
