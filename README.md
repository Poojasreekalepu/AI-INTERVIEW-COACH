# 🎯 AI Interview Coach

## Overview

AI Interview Coach is an intelligent interview preparation platform that helps students, fresh graduates, and job seekers practice company-specific interview questions using Generative AI.

Unlike traditional interview practice systems that rely on fixed question banks, this application dynamically generates unique interview questions using Google Gemini AI and evaluates candidate responses with AI-powered feedback.

The goal is to simulate real interview experiences and help users improve their technical knowledge, communication skills, and interview confidence.


## Problem Statement

Many candidates face difficulties during interviews because:

* They lack realistic interview practice.
* They repeatedly encounter the same practice questions.
* They do not receive personalized feedback.
* They struggle to identify strengths and weaknesses.

AI Interview Coach addresses these challenges by generating dynamic interview questions and providing AI-based evaluations.


## Key Features

### 🚀 AI-Powered Question Generation

Questions are dynamically generated using Google Gemini AI based on:

* Company
* Domain
* Difficulty Level

This ensures fresh and relevant interview questions.


### 🏢 Company-Specific Preparation

Users can prepare for interviews of companies such as:

* Google
* Amazon
* Microsoft
* Meta
* Apple
* Netflix
* TCS
* Infosys
* Wipro
* Accenture
* Cognizant
* Capgemini
* Deloitte


### 📚 Multiple Interview Domains

Supported domains include:

* HR
* Python
* Data Structures & Algorithms
* Operating Systems
* Database Management Systems
* Artificial Intelligence & Machine Learning


### 🎯 Difficulty Levels

Users can select:

* Easy
* Medium
* Hard

to match their preparation level.


### 🤖 AI Answer Evaluation

Google Gemini AI evaluates candidate responses based on:

* Relevance
* Technical Accuracy
* Communication Skills
* Completeness

The system provides:

* Scores
* Strengths
* Weaknesses
* Improvement Suggestions


### 🔄 Reduced Question Repetition

Previously generated questions are tracked during the session and avoided whenever possible, creating a more diverse interview experience.


## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini 2.5 Flash

### Version Control

* Git & GitHub


## Project Architecture

## Architecture

User Input
-> Company Selection
-> Domain Selection
-> Difficulty Selection
-> Gemini AI Question Generation
-> User Response
-> Gemini AI Evaluation
-> Feedback Report


## Installation

### Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### Navigate to Project Directory

```bash
cd AI-Interview-Coach
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Requirements

```text
streamlit
google-generativeai
```

---

## Future Enhancements

### 📊 Performance Dashboard

* Average Score
* Best Score
* Interview Analytics

### 📝 Interview History

Store and view previous interview attempts.

### 📄 Resume-Based Interview Generation

Generate personalized questions from uploaded resumes.

### 🎤 Mock Interview Mode

Interactive conversational interview sessions.


## Target Users

* Students preparing for placements
* Internship applicants
* Fresh graduates
* Software engineering candidates
* Technical interview aspirants


## Project Highlights

✅ Company-Specific Interview Preparation

✅ AI-Generated Dynamic Questions

✅ AI-Based Answer Evaluation

✅ Difficulty-Based Learning

✅ Reduced Question Repetition

✅ Modern Streamlit Interface


## Author

Developed as an AI-powered interview preparation platform for an Open Source Hackathon using Python, Streamlit, and Google Gemini AI.
Pooja Sree
