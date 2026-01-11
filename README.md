# Kharagpur Data Science Hackathon 2026 (KDSH 2026)

## Team Name
Sanjivani Squad

## Track
Track A – Systems Reasoning with NLP and Generative AI

---

## 📌 Problem Overview

Large Language Models often struggle with global consistency and causal reasoning
when dealing with long-form narratives (100k+ words).
This challenge focuses on determining whether a hypothetical character backstory
is logically and causally consistent with the complete narrative of a novel.

The task is framed as a binary classification problem:
- 1 → Backstory is consistent
- 0 → Backstory contradicts the narrative

---

## 🧠 Our Approach

- Treat the task as a constraint-based reasoning problem
- Break long narratives into manageable chunks
- Use Pathway for long-context ingestion and retrieval
- Retrieve evidence relevant to backstory claims
- Perform causal and consistency checks across narrative timelines
- Output a final binary decision with a short rationale

---

## 🛠️ Tech Stack

- Python
- Pathway Framework
- NLP-based retrieval & reasoning
- Pandas / NumPy

---

## 📁 Project Structure

Sanjivani_Squad_KDSH_2026/
│
├── code/
│   ├── main.py              # Entry point – runs full pipeline
│   ├── data_loader.py       # Loads narrative & backstory
│   ├── retriever.py         # Pathway-based long-context retrieval
│   ├── reasoning.py         # Consistency & causal reasoning logic
│   ├── config.py            # Global configuration
│   └── requirements.txt     # Python dependencies
│
├── report/
│   └── KDSH_Report.pdf      # Final 10-page report
│
├── results.csv              # Final predictions output
│
└── README.md                # Project overview & run instructions


---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
pip install -r code/requirements.txt

### 2️⃣ Run the Pipeline
python code/main.py

---

## 📊 Output

The results.csv file contains:
- story_id
- prediction (1 or 0)
- rationale

---

## ⚠️ Limitations

- Heuristic-based contradiction detection
- Limited deep causal modeling
- Scope for stronger LLM-based reasoning

---

## 👥 Team

Sanjivani Squad  
Kharagpur Data Science Hackathon 2026

