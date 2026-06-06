import os
import pandas as pd
import re
import streamlit as st
import google.generativeai as genai

# =========================
# GEMINI SETUP
# =========================

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

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
                # SAVE HISTORY
                # =========================

                score_match = re.search(
                    r"(\d+)\s*/\s*20",
                    evaluation.text
                )

                if score_match:
                    score = int(
                        score_match.group(1)
                    )
                else:
                    score = 0

                new_data = pd.DataFrame([
                    {
                        "Company": company,
                        "Domain": domain,
                        "Difficulty": difficulty,
                        "Score": score
                    }
                ])

                if os.path.exists(
                    "history.csv"
                ):

                    history = pd.read_csv(
                        "history.csv"
                    )

                    history = pd.concat(
                        [
                            history,
                            new_data
                        ],
                        ignore_index=True
                    )

                else:

                    history = new_data

                history.to_csv(
                    "history.csv",
                    index=False
                )

# =========================
# DASHBOARD
# =========================

st.markdown("---")

if st.button("📊 View Dashboard"):

    if os.path.exists("history.csv"):

        history = pd.read_csv(
            "history.csv"
        )

        if len(history) > 0:

            st.subheader(
                "📊 Dashboard"
            )

            st.metric(
                "Total Interviews",
                len(history)
            )

            st.metric(
                "Average Score",
                round(
                    history["Score"].mean(),
                    2
                )
            )

            st.metric(
                "Best Score",
                history["Score"].max()
            )

            st.write(
                "### Most Practiced Domain"
            )

            st.write(
                history["Domain"].mode()[0]
            )

            st.write(
                "### Most Practiced Company"
            )

            st.write(
                history["Company"].mode()[0]
            )

            st.write(
                "### Interview History"
            )

            st.dataframe(
                history
            )

        else:

            st.warning(
                "No interview history available."
            )

    else:

        st.warning(
            "history.csv not found."
        )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Built using Streamlit and Google Gemini AI"
)