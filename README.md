# AlgoCoach

**A Capstone Project for the Google AI Agents Intensive (Nov 2025)**

### What is this?
AlgoCoach is an AI Agent built to help competitive programmers. Instead of just solving problems, it acts like a teacher. It checks your code for "Time Limit Exceeded" errors (using a custom tool) and helps you optimize it.

### Features
* **Smart Agent:** Uses Google's **Gemini 1.5 Flash** model.
* **Tool Use:** Has a custom Python tool that counts loops to detect $O(n^2)$ complexity.
* **Helpful Hints:** Warns you if your code is too slow for large inputs.

### How to Run
1.  Open the `.ipynb` notebook in **Google Colab**.
2.  Get a free API Key from [Google AI Studio](https://aistudio.google.com/).
3.  Enter your API Key in the first cell.
4.  Run all cells to start the chat!

###  Tech Stack
* Python
* Google Gen AI SDK
* Gradio (for the chat interface)
