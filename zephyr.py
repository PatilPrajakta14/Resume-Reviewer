import streamlit as st
import fitz  # PyMuPDF for PDF extraction
from llama_cpp import Llama

st.set_page_config(page_title="Resume Reviewer with Llama_cpp", layout="centered")
st.title("Resume Reviewer (Llama_cpp)")

llm_chat = Llama(
    model_path=r"C:\Users\ppraj\OneDrive\Desktop\Workshop-GenAi & Prompt Engg\zephyr-7b-alpha.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=35
)

def get_chat_response(messages):
    response = llm_chat.create_chat_completion(messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

def extract_resume_text(file):
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        return "\n".join([page.get_text() for page in doc])

uploaded_file = st.file_uploader("Upload your resume (PDF only):", type="pdf")
if uploaded_file:
    resume_text = extract_resume_text(uploaded_file)
    st.subheader("Extracted Resume Text")
    st.text_area("Resume Text", resume_text, height=300)
    
    target_role = st.text_input("Target Job Role (e.g., Data Analyst, Software Engineer):")
    
    if st.button("Analyze Resume") and resume_text and target_role:
        # Step 1: Chain-of-Thought Summary
        with st.spinner("Generating chain-of-thought summary..."):
            cot_messages = [
                {"role": "system", "content": "You are a resume analyst."},
                {"role": "user", "content": (
                    "Provide a concise bullet-point chain-of-thought summary of the following resume. "
                    "Highlight key skills, work experiences, strengths, and potential areas for improvement. "
                    "Do not repeat the resume verbatim.\n\n"
                    f"Resume:\n{resume_text}"
                )}
            ]
            chain_of_thought = get_chat_response(cot_messages).strip()
        st.subheader("Chain-of-Thought Summary")
        st.write(chain_of_thought)
        
        # Step 2: Resume Review Feedback
        with st.spinner("Generating resume review feedback..."):
            review_messages = [
                {"role": "system", "content": "You are an experienced HR manager."},
                {"role": "user", "content": (
                    f"Based on the chain-of-thought summary below, provide detailed feedback on:\n"
                    "1. Strengths\n"
                    "2. Areas of improvement\n"
                    f"3. Skills missing for a {target_role} role\n\n"
                    f"Chain-of-Thought Summary:\n{chain_of_thought}"
                )}
            ]
            review_feedback = get_chat_response(review_messages)
        
        with st.spinner("Calculating ATS score..."):
            ats_messages = [
                {"role": "system", "content": "You are an applicant tracking system."},
                {"role": "user", "content": (
                    "Based on the chain-of-thought summary below, assign an ATS score between 0 and 100 for this resume. "
                    "Provide a brief explanation of how the score was determined.\n\n"
                    f"Chain-of-Thought Summary:\n{chain_of_thought}"
                )}
            ]
            ats_score = get_chat_response(ats_messages)

        # Display Results
        st.subheader("1. Resume Review Feedback")
        st.write(review_feedback)

        st.subheader("2. ATS Score")
        st.write(ats_score)

st.markdown("---")
st.caption("Built with Streamlit + llama_cpp")
