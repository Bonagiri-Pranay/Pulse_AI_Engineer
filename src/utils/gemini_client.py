import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_llm(system_prompt, user_prompt, model="models/gemini-2.5-flash"):
    prompt = system_prompt + "\n\n" + user_prompt
    response = genai.GenerativeModel(model).generate_content(prompt)
    return response.text
