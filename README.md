# 💰 IT Salary Predictor — India 2026

A data-driven salary prediction web application built with Python and Streamlit 
that estimates realistic salary ranges for IT professionals across major Indian cities.

🔗 Live Demo: https://salarypredictt.streamlit.app/

---

## 📌 Overview

This app predicts salary ranges for 15 major IT job roles across 10 Indian cities 
using a multi-factor estimation engine. Unlike simple flat-rate models, this app 
calculates salary based on role-specific base pay, experience growth rate, 
technical skills bonus, education level, and job type — giving users a realistic 
minimum, median, and maximum salary range.

---

## ✨ Features

- 15 IT job roles covered (Data Analyst, DevOps, Cloud Engineer, Cybersecurity, ML Engineer and more)
- 10 major Indian cities with individual base salaries per role
- 20+ technical skills with individual salary bonus values
- Education level multiplier (B.Tech, M.Tech, PhD, MCA and more)
- Internship vs Full-Time toggle for fresher-friendly estimates
- Salary range output — Minimum, Median, Maximum (±10% variance)
- Component-wise salary breakdown table
- City comparison bar chart to benchmark across locations
- Top 5 skill upgrade suggestions with potential salary impact

---

## 🧮 Salary Calculation Logic
```
Final Salary = (Base Salary + Experience Bonus + Skills Bonus)
               × Education Multiplier
               × Job Type Factor
```

| Component            | Description                                          |
|----------------------|------------------------------------------------------|
| Base Salary          | Fixed per role + city combination                    |
| Experience Bonus     | Years of experience × role-specific growth rate      |
| Skills Bonus         | Sum of bonuses for each selected technical skill     |
| Education Multiplier | Ranges from 0.80 (below 12th) to 1.25 (PhD)         |
| Job Type Factor      | Full-Time = ×1.00 / Internship = ×0.30              |
| Salary Range         | ±10% variance around median for Min / Max estimate   |

---

## 🖥️ Tech Stack

| Tool        | Usage                        |
|-------------|------------------------------|
| Python      | Core programming language    |
| Streamlit   | Web app UI and deployment    |
| Pandas      | Data handling and structuring |

---

## 📂 Project Structure
```
salary-predictor/
│
├── salary_app.py        # Main application file
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/rohan8265/salary-predictor.git
cd salary-predictor
```

**2. Install dependencies**
```bash
pip install streamlit pandas
```

**3. Run the app**
```bash
streamlit run salary_app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 📊 Job Roles Covered

| Track              | Roles                                                      |
|--------------------|------------------------------------------------------------|
| Data               | Data Analyst, Data Scientist, ML Engineer, AI/ML Research  |
| Software           | Software Engineer, Full Stack, Frontend, Backend Developer |
| Infrastructure     | DevOps Engineer, Cloud Engineer, Network Engineer, DBA     |
| Security           | Cybersecurity Analyst                                      |
| Business           | Business Analyst, Product Manager (Tech)                   |

---

## 🏙️ Cities Covered

Bangalore · Mumbai · Delhi NCR · Hyderabad · Pune · Chennai · 
Kolkata · Ahmedabad · Jaipur · Remote

---

## 💡 Key Insights from the Model

- Bangalore pays 30–40% more than Tier-2 cities like Jaipur for the same role
- AI/ML Research Engineer and Product Manager have the highest salary ceilings
- Deep Learning and Kubernetes are the highest-bonus skills in the model
- M.Tech holders earn ~12% more than B.Tech for the same role and experience
- Internship salaries are modelled at 30% of full-time equivalent

---

## 🙋 Author

**Rohan Gupta**  
B.Tech CSE — Lovely Professional University  
📧 guptarohan919284@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/guptarohann/)  
🐙 [GitHub](https://github.com/rohan8265)

---

## 📄 Disclaimer

Salary estimates are based on approximate Indian IT market data for 2025. 
Actual offers vary by company, interview performance, and negotiation skills.
