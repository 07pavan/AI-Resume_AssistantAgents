# 🤖 AI Resume Assistant

> **An intelligent, AI-powered resume analysis and optimization tool built with Streamlit and Groq (Llama 3.1).**  
> Upload your resume — get instant feedback, ATS scoring, job matching, cover letters, and real job listings, all in one place.

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai-resumeassistantagents-pavan.streamlit.app/)

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **ATS Score** | Evaluates your resume against Applicant Tracking System (ATS) criteria with a score out of 100, highlighting strengths, weaknesses, and missing keywords |
| 🔍 **Resume Analysis** | Deep analysis of your skills, experience, projects, and ATS compatibility by a simulated expert recruiter |
| ✨ **Resume Improvement** | AI-generated, rewritten version of your resume with professional language and optimized content |
| 📄 **PDF Export** | Download the improved resume as a clean, formatted PDF instantly |
| 🎯 **Job Match Score** | Compares your resume against a target job role and returns a match percentage, matching skills, missing skills, and actionable recommendations |
| 💼 **Job Suggestions** | Fetches live job listings from the web via JSearch API (RapidAPI) based on your target role |
| ✉️ **Cover Letter Generator** | Generates a personalized, role-specific cover letter from your resume content |

---

## 🏗️ Project Architecture

```
ai-resume_assistantAgents/
│
├── app.py                    # Streamlit frontend — main entry point
│
├── llm/
│   └── llm_client.py         # Groq API client (Llama 3.1-8b-instant) with retry logic
│
├── parser/
│   └── resume_parser.py      # PDF & DOCX resume text extractor (pypdf, python-docx)
│
├── pipeline/
│   ├── analyzer.py           # Resume analysis pipeline
│   ├── improver.py           # Resume rewriting pipeline
│   ├── ats_score.py          # ATS evaluation pipeline
│   ├── job_matcher.py        # Resume ↔ Job role match scoring
│   ├── jobs.py               # Live job listing fetcher (JSearch / RapidAPI)
│   └── cover_letter.py       # Cover letter generation pipeline
│
├── utils/
│   └── pdf_generator.py      # ReportLab-based PDF export utility
│
├── requirements.txt          # Python dependencies
├── .env                      # API keys (not committed to Git)
└── .gitignore
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **LLM** | [Groq Cloud](https://groq.com/) — `llama-3.1-8b-instant` |
| **Resume Parsing** | `pypdf`, `python-docx` |
| **Job Listings API** | [JSearch via RapidAPI](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) |
| **PDF Generation** | `reportlab` |
| **Environment Management** | `python-dotenv` |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/07pavan/AI-Resume_AssistantAgents.git
cd AI-Resume_AssistantAgents
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
RAPIDAPI_KEY=your_rapidapi_key_here
```

- Get your **Groq API key** → [console.groq.com](https://console.groq.com)
- Get your **RapidAPI key** → [rapidapi.com](https://rapidapi.com) (subscribe to the [JSearch API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch))

> ⚠️ **Never commit your `.env` file to Git.** It is already listed in `.gitignore`.

### 5. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🧠 How It Works

1. **Upload** your resume (`.pdf` or `.docx`)
2. **Select** the features you want (analysis, improvement, ATS score, job match, job listings, cover letter)
3. **Enter** your target job role and search query
4. **Click** `Run AI Assistant`
5. The pipeline sends your resume text to **Groq's Llama 3.1** LLM for each selected task
6. Results are displayed in the app — and you can **download** the improved resume as a PDF

---

## 📦 Dependencies

```
streamlit
groq
pypdf
python-docx
reportlab
requests
python-dotenv
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Keys Required

| API | Purpose | Free Tier |
|---|---|---|
| [Groq](https://console.groq.com) | LLM inference (Llama 3.1) | ✅ Yes |
| [RapidAPI / JSearch](https://rapidapi.com) | Live job listings | ✅ Yes (limited) |

---

## 📸 App Preview

🔗 **[Try it live → ai-resumeassistantagents-pavan.streamlit.app](https://ai-resumeassistantagents-pavan.streamlit.app/)**

> Upload → Select Features → Run → Get AI-powered results instantly.

**Available Modes:**
- 📊 ATS Resume Score
- 🔍 Resume Analysis
- ✨ AI-Improved Resume + PDF Download
- 🎯 Resume ↔ Job Match Score
- 💼 Live Job Suggestions
- ✉️ AI Cover Letter

---

## 🛡️ Notes

- API responses are **cached** using `@st.cache_data` to minimize unnecessary API calls during the same session.
- The LLM client includes **automatic retry logic** (3 attempts with a 3-second delay) to handle transient API errors gracefully.
- Job suggestions are cached with a **10-minute TTL** (`ttl=600`) to rate-limit external API usage.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">
  Built with ❤️ using Streamlit + Groq + Llama 3.1
</div>
