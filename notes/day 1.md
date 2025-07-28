# 📘 Day 1 Notes – Project Setup & Speech Recognition Foundation

## ✅ Goals Completed:
- Set up the project environment
- Learned basics of Speech Recognition in Python

---

## 🛠️ Project Setup

### Folder Structure:
```
project/
│
├── .venv/                      # Python virtual environment
├── .github/workflows/         # GitHub Actions (CI/CD)
├── data/
│   ├── raw/                   # Raw audio files
│   └── transcripts/           # Text transcripts from speech
├── src/                       # Source code
├── notebooks/                 # Jupyter notebooks (for exploration)
├── tests/                     # Unit tests
├── utils/                     # Utility scripts
├── outputs/                   # Output files (e.g., model, logs)
├── README.md                  # Project description
└── requirements.txt           # Dependencies
```

---

## 💻 VS Code Environment

- Created and activated a virtual environment using:
  ```bash
  python -m venv .venv
  ```

- Activated in PowerShell with:
  ```bash
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  .venv\Scripts\Activate
  ```

- Installed basic packages:
  ```bash
  pip install speechrecognition
  pip install pyaudio
  pip install wave
  ```

---

## 🌐 GitHub Setup

- Initialized Git and connected to remote repo:
  ```bash
  git init
  git remote add origin https://github.com/yourusername/project.git
  git add .
  git commit -m "Initial commit"
  git branch -M main
  git push -u origin main
  ```

- Created a **GitHub Personal Access Token** and used it for authentication.
- Solved permission error by enabling `workflow` scope in the token.

---

## 🧠 Concepts Learned

- What is Speech Recognition?
- How the `SpeechRecognition` Python library works
- How to set up Python environment using VS Code
- GitHub integration and Git workflow using VS Code and terminal

---

## 📌 Next Step Preview (Day 2)

- Implement basic speech-to-text using mic or audio files
- Learn and use the `SpeechRecognition` and `pyaudio` libraries
- Save transcript to file and update GitHub

---

🗓️ Date: [Enter the actual date here]  
🧑‍💻 Completed by: Srihari (Creator | Coder | Hustler)
