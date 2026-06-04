import streamlit as st
import google.generativeai as genai

# =========================
# GEMINI SETUP
# =========================

genai.configure(api_key="YOUR_GOOGLE_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================

if "asked_questions" not in st.session_state:
    st.session_state.asked_questions = []

# =========================
# TITLE
# =========================

st.title("🎯 AI Interview Coach")

st.write(
    "Practice company-specific interview questions generated and evaluated by AI."
)

# =========================
# COMPANIES
# =========================

companies = [
    "Google",
    "Amazon",
    "Microsoft",
    "Meta",
    "Apple",
    "Netflix",
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Cognizant",
    "Capgemini",
    "Deloitte"
]

# =========================
# SIDEBAR
# =========================

st.sidebar.header("Interview Settings")

company = st.sidebar.selectbox(
    "Select Company",
    companies
)

domain = st.sidebar.selectbox(
    "Select Domain",
    [
        "HR",
        "Python",
        "DSA",
        "Operating Systems",
        "DBMS",
        "AI/ML"
    ]
)

difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

st.success(
    f"🏢 {company} | 📚 {domain} | 🎯 {difficulty}"
)

# =========================
# GENERATE QUESTION
# =========================

if st.button("🎲 Generate AI Question"):

    with st.spinner("Generating question..."):

        prompt = f"""
Generate ONE unique {difficulty} level interview question.

Company: {company}
Domain: {domain}

Avoid these previously asked questions:
{st.session_state.asked_questions}

Rules:
- Return ONLY the interview question.
- Do not provide answers.
- Make it realistic.
- Do not repeat previous questions.
"""

        response = model.generate_content(prompt)

        question = response.text.strip()

        st.session_state.question = question

        st.session_state.asked_questions.append(question)

# =========================
# DISPLAY QUESTION
# =========================

if "question" in st.session_state:

    st.subheader("📝 AI Generated Question")

    st.info(st.session_state.question)

    answer = st.text_area(
        "Enter Your Answer",
        height=200
    )

    # =========================
    # AI EVALUATION
    # =========================

    if st.button("📊 Evaluate Answer"):

        if answer.strip() == "":
            st.warning("Please enter an answer first.")
        else:

            with st.spinner("AI is evaluating your answer..."):

                evaluation_prompt = f"""
You are an expert interviewer.

Interview Question:
{st.session_state.question}

Candidate Answer:
{answer}

Evaluate the answer using:

1. Relevance (out of 5)
2. Technical Accuracy (out of 5)
3. Communication (out of 5)
4. Completeness (out of 5)

Then provide:

- Total Score (out of 20)
- Strengths
- Weaknesses
- Suggestions for Improvement

Format the response neatly.
"""

                evaluation = model.generate_content(
                    evaluation_prompt
                )

                st.subheader(
                    "📊 AI Evaluation Report"
                )

                st.markdown(
                    evaluation.text
                )

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption(
    "Built using Streamlit and Google Gemini AI"
)