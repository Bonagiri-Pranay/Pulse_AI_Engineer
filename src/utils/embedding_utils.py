import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_embeddings(sentences):
    """
    Uses Gemini's embed_content() to generate embeddings.
    Works for models supporting: ['embedContent']
    Example model: models/text-embedding-004
    """

    embeddings = []

    for text in sentences:
        response = genai.embed_content(
            model="models/text-embedding-004",
            content=text
        )
        embeddings.append(response['embedding'])

    return embeddings
