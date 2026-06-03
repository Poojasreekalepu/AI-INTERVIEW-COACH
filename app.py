import streamlit as st
import json
import random

# Page Config
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="centered"
)

# Load Questions
with open("questions.json", "r") as file:
    questions = json.load(file)

# Title
st.title("🎯 AI Interview Coach")
st.write("Practice interview questions and evaluate your answers.")

# Sidebar
st.sidebar.header("Interview Settings")

domain = st.sidebar.selectbox(
    "Select Domain",
    list(questions.keys())
)

difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Generate Question
if st.button("🎲 Generate Question"):

    selected_question = random.choice(
        questions[domain][difficulty]
    )

    st.session_state.question_data = selected_question

# Display Question
if "question_data" in st.session_state:

    q = st.session_state.question_data

    st.subheader("📝 Interview Question")

    st.info(q["question"])

    answer = st.text_area(
        "Enter Your Answer",
        height=150
    )

    if st.button("📊 Evaluate Answer"):

        answer_lower = answer.lower()

        matched_keywords = []

        relevance_score = 0

        # Keyword Matching
        for keyword in q["keywords"]:

            if keyword.lower() in answer_lower:

                relevance_score += 1
                matched_keywords.append(keyword)

        # Max 5 Marks
        relevance_score = min(relevance_score, 5)

        # Technical Score
        technical_score = relevance_score

        # Communication Score
        word_count = len(answer.split())

        if word_count >= 60:
            communication_score = 5
        elif word_count >= 40:
            communication_score = 4
        elif word_count >= 20:
            communication_score = 3
        elif word_count >= 10:
            communication_score = 2
        else:
            communication_score = 1

        # Completeness Score
        completeness_score = relevance_score

        total_score = (
            relevance_score
            + technical_score
            + communication_score
            + completeness_score
        )

        # Report
        st.markdown("---")
        st.subheader("📊 AI Interview Evaluation Report")

        st.write(f"✅ Relevance: {relevance_score}/5")
        st.write(f"✅ Technical Accuracy: {technical_score}/5")
        st.write(f"✅ Communication: {communication_score}/5")
        st.write(f"✅ Completeness: {completeness_score}/5")

        st.markdown("---")

        st.success(f"🎯 Total Score: {total_score}/20")

        # Performance Level
        if total_score >= 18:
            st.success("🏆 Performance Level: Excellent")

        elif total_score >= 15:
            st.success("👍 Performance Level: Good")

        elif total_score >= 10:
            st.warning("⚡ Performance Level: Average")

        else:
            st.error("📚 Performance Level: Needs Improvement")

        # Keywords
        st.markdown("### 🔍 Keywords Matched")

        if matched_keywords:

            for keyword in matched_keywords:
                st.write(f"✔️ {keyword}")

        else:
            st.write("No important keywords detected.")

        # Suggestions
        st.markdown("### 💡 Suggestions")

        if total_score >= 18:

            st.write(
                "Excellent answer. Try adding real-world examples for an even stronger response."
            )

        elif total_score >= 15:

            st.write(
                "Good answer. Include a few more technical concepts."
            )

        elif total_score >= 10:

            st.write(
                "Your answer is partially correct. Cover more key points."
            )

        else:

            st.write(
                "Review the topic and try again with a more detailed explanation."
            )

        # Word Count
        st.markdown("### 📈 Statistics")
        st.write(f"Words Written: {word_count}")