# 🎯 AI Interview Coach

## Problem Statement

Many students and job seekers struggle to prepare for interviews because they rely on static question banks and do not receive meaningful feedback on their answers. Traditional interview preparation platforms often repeat the same questions and lack personalized evaluation.

AI Interview Coach solves this problem by generating company-specific interview questions using AI and providing instant feedback on candidate responses.


## Project Overview

AI Interview Coach is a web application that helps users practice interviews in different domains such as Python, DSA, Operating Systems, DBMS, AI/ML, and HR. The system generates unique interview questions using Google Gemini AI and evaluates user answers with detailed feedback.


## Features

* AI-generated interview questions
* Company-specific interview preparation
* Multiple interview domains

  * HR
  * Python
  * DSA
  * Operating Systems
  * DBMS
  * AI/ML
* Easy, Medium, and Hard difficulty levels
* AI-powered answer evaluation
* Feedback with strengths and improvement suggestions
* Reduced question repetition
* Interview history tracking
* Performance dashboard


## Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini 2.5 Flash

### Data Storage

* CSV (history tracking)

### Version Control

* GitHub


## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Open Project Folder

```bash
cd AIINTERVIEWCOACH
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Add Gemini API Key

Replace:

```python
genai.configure(api_key="YOUR_GOOGLE_API_KEY")
```

with your Gemini API key.

### 5. Run the Application

```bash
streamlit run app.py
```



## Project Workflow

1. User selects a company.
2. User selects a domain.
3. User selects difficulty level.
4. Gemini AI generates a unique interview question.
5. User submits an answer.
6. Gemini AI evaluates the response.
7. Feedback and score are displayed.
8. Results are stored in interview history.
9. Dashboard displays performance statistics.


## Screenshots

### Home Page

<img width="1911" height="996" alt="image" src="https://github.com/user-attachments/assets/4cc3c133-906f-47b2-b6ff-608cf5c447f8" />


### AI Generated Question

<img width="1876" height="971" alt="image" src="https://github.com/user-attachments/assets/9af672f8-3c71-42a0-9a8b-fe72b95659f3" />


### AI Evaluation Report

<img width="414" height="949" alt="image" src="https://github.com/user-attachments/assets/4b774505-47a7-485d-93cc-28ebd5add03e" />


### Dashboard

<img width="980" height="911" alt="image" src="https://github.com/user-attachments/assets/c3b432fe-95ec-439c-9441-e7c715cf0af3" />


## Future Enhancements

* Resume-based interview questions
* Voice-based mock interviews
* Advanced analytics dashboard
* Personalized learning recommendations
* Export interview reports

---

## Author

Developed for Open Source Hackathon 2026 using Python, Streamlit, and Google Gemini AI.
Pooja Sree Kalepu
