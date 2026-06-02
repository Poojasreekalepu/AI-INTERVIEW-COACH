import streamlit as st
import json
import random

# Load questions
with open("questions.json", "r") as file:
    questions = json.load(file)

st.title("🎯 AI Interview Coach")

st.write("Practice interview questions and get evaluated.")

# Domain Selection
domain = st.selectbox(
    "Select Domain",
    list(questions.keys())
)

# Generate Question
if st.button("Generate Question"):
    selected_question = random.choice(questions[domain])

    st.session_state.question_data = selected_question

# Show Question
if "question_data" in st.session_state:

    q = st.session_state.question_data

    st.subheader("Interview Question")

    st.write(q["question"])

    answer = st.text_area(
        "Enter Your Answer"
    )

    if st.button("Evaluate Answer"):

        answer_lower = answer.lower()

        relevance = 0

        matched_keywords = []

        # Keyword Matching
        for keyword in q["keywords"]:

            if keyword.lower() in answer_lower:

                relevance += 1
                matched_keywords.append(keyword)

        # Score Calculation

        relevance_score = min(relevance, 5)

        technical_score = min(relevance, 5)

        communication_score = 4 if len(answer.split()) > 20 else 2

        completeness_score = min(relevance, 5)

        total_score = (
            relevance_score
            + technical_score
            + communication_score
            + completeness_score
        )

        st.markdown("---")

        st.subheader("📊 AI Interview Evaluation Report")

        st.write(
            f"Relevance : {relevance_score}/5"
        )

        st.write(
            f"Technical Accuracy : {technical_score}/5"
        )

        st.write(
            f"Communication : {communication_score}/5"
        )

        st.write(
            f"Completeness : {completeness_score}/5"
        )

        st.markdown("---")

        st.write(
            f"## Total Score : {total_score}/20"
        )

        # Performance Level

        if total_score >= 18:
            st.success("Excellent Performance")
        elif total_score >= 15:
            st.success("Good Performance")
        elif total_score >= 10:
            st.warning("Average Performance")
        else:
            st.error("Needs Improvement")

        # Keywords Found

        st.markdown("### ✅ Keywords Matched")

        if matched_keywords:

            for keyword in matched_keywords:
                st.write(f"• {keyword}")

        else:
            st.write(
                "No important keywords found."
            )

        # Suggestions

        st.markdown("### 💡 Suggestions")

        if total_score >= 18:
            st.write(
                "Excellent answer. Add a real-world example for even better impact."
            )

        elif total_score >= 15:
            st.write(
                "Good answer. Include more technical details."
            )

        elif total_score >= 10:
            st.write(
                "Answer is partially correct. Cover more important concepts."
            )

        else:
            st.write(
                "Review the topic and try again with a more detailed explanation."
            )