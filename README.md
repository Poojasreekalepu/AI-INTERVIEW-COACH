# AI-INTERVIEW-COACH
AI-powered interview preparation platform that provides interview questions, answer evaluation, scoring, and feedback for students.

## Overview
AI Interview Coach is an interactive interview preparation platform designed to help students and job seekers practice technical and HR interview questions.

The application provides domain-specific interview questions, evaluates user responses, and generates performance scores based on relevance, technical accuracy, communication, and completeness.

This project aims to improve interview confidence and help users identify areas for improvement through continuous practice.

## Problem Statement

Many students struggle during interviews because they:

* Lack interview practice
* Do not know how to structure answers
* Have difficulty identifying weak areas
* Need personalized feedback

AI Interview Coach provides a simple platform to simulate interview experiences and track performance.

## Features

### ✅ Domain-Based Interview Preparation

Users can choose interview questions from multiple domains:

* HR
* Python
* Data Structures & Algorithms (DSA)
* Operating Systems (OS)
* Database Management Systems (DBMS)
* Artificial Intelligence & Machine Learning (AI/ML)

### ✅ Difficulty Levels

Each domain contains:

* Easy Questions
* Medium Questions
* Hard Questions

This allows users to gradually improve their interview skills.

### ✅ Random Question Generation

The system randomly selects a question from the chosen domain and difficulty level.

### ✅ Answer Evaluation

User answers are evaluated based on:

1. Relevance (5 Marks)
2. Technical Accuracy (5 Marks)
3. Communication Skills (5 Marks)
4. Completeness (5 Marks)

Total Score: 20 Marks

### ✅ Performance Report

The application generates:

* Detailed Score Report
* Performance Level
* Keyword Matching Analysis
* Improvement Suggestions

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Data Storage

* JSON

## Project Structure

AI-Interview-Coach/

├── app.py

├── questions.json

├── requirements.txt

├── README.md

## How to Run

### Step 1

Clone the repository

git clone YOUR_REPOSITORY_LINK

### Step 2

Navigate to project folder

cd AI-Interview-Coach

### Step 3

Install dependencies

pip install -r requirements.txt

### Step 4

Run application

streamlit run app.py

## Current Functionalities

* Domain Selection
* Difficulty Selection
* Random Question Generation
* Answer Evaluation
* Score Calculation
* Feedback Generation

## Future Enhancements

### Gemini AI Integration

AI-powered evaluation of answers based on:

* Technical Accuracy
* Communication Skills
* Confidence Level
* Relevance

### Resume-Based Question Generation

Users can upload resumes and receive personalized interview questions.

### Interview History Tracking

Store previous interview attempts and performance records.

### Performance Dashboard

Visualize:

* Average Score
* Best Score
* Strongest Domain
* Weakest Domain

## Target Users

* Students preparing for placements
* Internship applicants
* Fresh graduates
* Technical interview candidates

## Author

Developed as part of an Open Source Hackathon project to create an intelligent interview preparation platform.
Pooja Sree
