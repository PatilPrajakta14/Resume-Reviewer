# Resume reviewer

A Streamlit-based web app that uses `llama_cpp` to analyze PDF resumes. Upload your resume, get a chain-of-thought summary, HR-style feedback, and an ATS score—all powered by a local Llama model.

---

## 🚀 Features

- **PDF Extraction**  
  Reads and extracts text from uploaded PDF resumes using PyMuPDF (`fitz`).

- **Chain-of-Thought Summary**  
  Generates concise bullet-point reasoning about key skills, experiences, and improvement areas.

- **HR-Style Feedback**  
  Provides detailed strengths, weaknesses, and missing skills for a specified target role.

- **ATS Scoring**  
  Simulates an Applicant Tracking System to assign a 0–100 score and explain the result.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)  
- **PDF Extraction**: [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)  
- **LLM Backend**: [llama_cpp](https://github.com/abetlen/llama-cpp-python)  
- **Model**: Zephyr-7B (gguf format) via `llama_cpp.create_chat_completion`

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/PatilPrajakta14/Resume-Reviewer.git
   ```
2. Create & activate a virtual environment
    ```bash
   python3 -m venv .venv
   source .venv/bin/activate # Linux / macOS
   .\.venv\Scripts\activate # Windows
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Download or place your Llama model
Put your .gguf model file (like zephyr-7b-alpha.Q4_K_M.gguf) in a known path

## ⚙️ Configuration
Edit the model path in app.py (or whichever Python file you use):
```python
llm_chat = Llama(
    model_path="C:/path/to/zephyr-7b-alpha.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=35
)
```
Adjust n_threads, n_gpu_layers, and n_ctx according to your hardware.

## 🚀 Usage
1. Run the app
```bash
streamlit run app.py
```
2. In your browser

 - Upload a PDF resume.

 - Enter your target job role (e.g., “Data Analyst”).

 - Click Analyze Resume.

3. See results

 - Chain-of-Thought Summary

 - Resume Review Feedback

 - ATS Score and explanation
