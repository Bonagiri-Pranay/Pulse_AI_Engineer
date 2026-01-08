from src.utils.gemini_client import call_llm
import re

def extract_topics_agent(texts):
    system_prompt = """
    You are a high-recall topic extraction agent.
    Extract all issues, complaints, and requests as short topic phrases (max 5 words).
    Output ONLY a Python list. No markdown, no explanations, no code fences.
    Example:
    ["delivery delay", "food stale", "app crash"]
    """

    user_prompt = "\n\n".join(texts)
    output = call_llm(system_prompt, user_prompt)

    # --- CLEAN GEMINI OUTPUT ---
    # Remove ```python blocks if present
    output = re.sub(r"```.*?```", "", output, flags=re.DOTALL)
    output = output.replace("```", "")
    output = output.strip()

    # Force output into proper list format if Gemini misbehaves
    if not output.startswith("["):
        # try to extract list with regex
        match = re.search(r"\[(.*?)\]", output, re.DOTALL)
        if match:
            output = "[" + match.group(1) + "]"

    try:
        return eval(output)  # now safe
    except:
        print("--- RAW GEMINI OUTPUT ---")
        print(output)
        raise ValueError("Gemini did not return a valid Python list.")
