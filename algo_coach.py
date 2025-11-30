!pip install -q -U google-generativeai gradio

import google.generativeai as genai
import gradio as gr
import os

os.environ["GOOGLE_API_KEY"] = ""   
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model_name = "gemini-2.0-flash"
print(f"✅ Using Model: {model_name}")

def analyze_code_structure(code_snippet: str):
    loop_count = code_snippet.count("for ") + code_snippet.count("while ")
    return {
        "loops_found": loop_count,
        "complexity_warning": "High Risk (Potential O(n^2))" if loop_count > 1 else "Low Risk",
        "recommendation": "Check constraints. If N > 10^4, this will TLE."
        if loop_count > 1 else "Good structure."
    }

tools_list = [analyze_code_structure]

try:
    model = genai.GenerativeModel(
        model_name,
        tools=tools_list,
        system_instruction="""
        You are AlgoCoach, an expert Competitive Programming mentor.

        RULES:
        1. Guide students to optimize code.
        2. NEVER just give the answer.
        3. ALWAYS call analyze_code_structure first.
        4. If tool reports High Risk, warn about Big-O and TLE.
        """
    )
    print(" Model initialized successfully.")
except Exception as e:
    print(f" Error initializing model: {e}")

chat = model.start_chat(enable_automatic_function_calling=True)

def chat_function(message, history):
    try:
        response = chat.send_message(message)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⚠️ Quota Exceeded. Please wait 60 seconds — Free Tier Limitation!"
        return f"Error: {str(e)}"

demo = gr.ChatInterface(
    fn=chat_function,
    title="AlgoCoach 🧠",
    description=f"Running on {model_name}. Paste your code to check complexity!",
    examples=["Check this code: for i in range(n): for j in range(n): print(i,j)"]
)

demo.launch(debug=True)
