import streamlit as st
import pandas as pd

st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="centered")

# ── Salary base data: (role → city → base_salary) ──────────────────────────
SALARY_DATA = {
    "Data Analyst": {
        "Bangalore":  500000, "Mumbai":    480000, "Delhi NCR": 460000,
        "Hyderabad":  470000, "Pune":      450000, "Chennai":   440000,
        "Kolkata":    380000, "Ahmedabad": 360000, "Jaipur":    340000, "Remote": 420000,
    },
    "Data Scientist": {
        "Bangalore":  900000, "Mumbai":    860000, "Delhi NCR": 840000,
        "Hyderabad":  820000, "Pune":      780000, "Chennai":   760000,
        "Kolkata":    600000, "Ahmedabad": 560000, "Jaipur":    520000, "Remote": 750000,
    },
    "Machine Learning Engineer": {
        "Bangalore": 1000000, "Mumbai":    950000, "Delhi NCR": 920000,
        "Hyderabad":  880000, "Pune":      840000, "Chennai":   800000,
        "Kolkata":    650000, "Ahmedabad": 600000, "Jaipur":    560000, "Remote": 850000,
    },
    "Software Engineer": {
        "Bangalore":  800000, "Mumbai":    760000, "Delhi NCR": 740000,
        "Hyderabad":  720000, "Pune":      700000, "Chennai":   680000,
        "Kolkata":    520000, "Ahmedabad": 490000, "Jaipur":    460000, "Remote": 680000,
    },
    "DevOps Engineer": {
        "Bangalore":  900000, "Mumbai":    860000, "Delhi NCR": 840000,
        "Hyderabad":  800000, "Pune":      780000, "Chennai":   740000,
        "Kolkata":    580000, "Ahmedabad": 540000, "Jaipur":    500000, "Remote": 780000,
    },
    "Cloud Engineer": {
        "Bangalore":  950000, "Mumbai":    900000, "Delhi NCR": 880000,
        "Hyderabad":  840000, "Pune":      800000, "Chennai":   760000,
        "Kolkata":    600000, "Ahmedabad": 560000, "Jaipur":    520000, "Remote": 820000,
    },
    "Cybersecurity Analyst": {
        "Bangalore":  850000, "Mumbai":    820000, "Delhi NCR": 810000,
        "Hyderabad":  780000, "Pune":      740000, "Chennai":   720000,
        "Kolkata":    560000, "Ahmedabad": 530000, "Jaipur":    490000, "Remote": 750000,
    },
    "Full Stack Developer": {
        "Bangalore":  850000, "Mumbai":    820000, "Delhi NCR": 800000,
        "Hyderabad":  770000, "Pune":      740000, "Chennai":   720000,
        "Kolkata":    560000, "Ahmedabad": 530000, "Jaipur":    490000, "Remote": 720000,
    },
    "Frontend Developer": {
        "Bangalore":  700000, "Mumbai":    680000, "Delhi NCR": 660000,
        "Hyderabad":  640000, "Pune":      620000, "Chennai":   600000,
        "Kolkata":    460000, "Ahmedabad": 440000, "Jaipur":    410000, "Remote": 600000,
    },
    "Backend Developer": {
        "Bangalore":  780000, "Mumbai":    750000, "Delhi NCR": 730000,
        "Hyderabad":  700000, "Pune":      680000, "Chennai":   660000,
        "Kolkata":    510000, "Ahmedabad": 480000, "Jaipur":    450000, "Remote": 660000,
    },
    "Business Analyst": {
        "Bangalore":  700000, "Mumbai":    720000, "Delhi NCR": 710000,
        "Hyderabad":  660000, "Pune":      640000, "Chennai":   620000,
        "Kolkata":    480000, "Ahmedabad": 460000, "Jaipur":    430000, "Remote": 580000,
    },
    "Database Administrator": {
        "Bangalore":  750000, "Mumbai":    720000, "Delhi NCR": 700000,
        "Hyderabad":  680000, "Pune":      650000, "Chennai":   630000,
        "Kolkata":    490000, "Ahmedabad": 460000, "Jaipur":    430000, "Remote": 620000,
    },
    "Network Engineer": {
        "Bangalore":  650000, "Mumbai":    640000, "Delhi NCR": 630000,
        "Hyderabad":  600000, "Pune":      580000, "Chennai":   560000,
        "Kolkata":    430000, "Ahmedabad": 410000, "Jaipur":    390000, "Remote": 540000,
    },
    "AI/ML Research Engineer": {
        "Bangalore": 1200000, "Mumbai":   1100000, "Delhi NCR":1050000,
        "Hyderabad": 1000000, "Pune":      950000, "Chennai":   900000,
        "Kolkata":    750000, "Ahmedabad": 700000, "Jaipur":    650000, "Remote":1000000,
    },
    "Product Manager (Tech)": {
        "Bangalore": 1500000, "Mumbai":   1450000, "Delhi NCR":1400000,
        "Hyderabad": 1300000, "Pune":     1200000, "Chennai":  1150000,
        "Kolkata":    900000, "Ahmedabad": 850000, "Jaipur":    800000, "Remote":1200000,
    },
}

# Experience multiplier per year (role-specific growth rate)
EXPERIENCE_MULTIPLIER = {
    "Data Analyst":               55000,
    "Data Scientist":             90000,
    "Machine Learning Engineer": 100000,
    "Software Engineer":          80000,
    "DevOps Engineer":            90000,
    "Cloud Engineer":             95000,
    "Cybersecurity Analyst":      85000,
    "Full Stack Developer":       80000,
    "Frontend Developer":         65000,
    "Backend Developer":          75000,
    "Business Analyst":           60000,
    "Database Administrator":     70000,
    "Network Engineer":           60000,
    "AI/ML Research Engineer":   120000,
    "Product Manager (Tech)":    150000,
}

# Skills bonus (flat bonus added on top)
SKILLS_BONUS = {
    "Python":           50000,
    "SQL":              40000,
    "Machine Learning": 80000,
    "Deep Learning":   100000,
    "Power BI":         40000,
    "Tableau":          40000,
    "AWS":              70000,
    "Azure":            70000,
    "GCP":              70000,
    "Docker":           60000,
    "Kubernetes":       80000,
    "React.js":         50000,
    "Node.js":          50000,
    "Java":             55000,
    "C++":              45000,
    "Go (Golang)":      75000,
    "Cybersecurity":    70000,
    "Networking":       45000,
    "Data Engineering": 75000,
    "Spark / Hadoop":   65000,
}

# Education multiplier
EDUCATION_MULTIPLIER = {
  #  "Below 12th":     0.80,
   # "12th / Diploma": 0.88,
    "B.Tech / B.E.":  1.00,
    "BCA / BSc CS":   0.95,
    "MCA / MSc":      1.08,
    "M.Tech / ME":    1.12,
    "MBA (Tech)":     1.15,
    "PhD":            1.25,
}

# ── UI ───────────────────────────────────────────────────────────────────────
st.title("💰 IT Salary Predictor — India 2026")
st.caption("Role-specific & city-specific salary estimates based on Indian IT market data.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    job_title  = st.selectbox("Job Role", list(SALARY_DATA.keys()))
    location   = st.selectbox("City", list(next(iter(SALARY_DATA.values())).keys()))
    education  = st.selectbox("Education Level", list(EDUCATION_MULTIPLIER.keys()))

with col2:
    skills     = st.multiselect(
        "Key Skills (select all you have)",
        list(SKILLS_BONUS.keys()),
        default=["Python"]
    )
    experience = st.slider("Years of Experience", 0, 25, 2)
    job_type   = st.radio("Job Type", ["Full-Time", "Internship"], horizontal=True)

st.markdown("---")

if st.button("🔍 Predict My Salary", use_container_width=True):

    base      = SALARY_DATA[job_title][location]
    exp_hike  = EXPERIENCE_MULTIPLIER[job_title] * experience
    skill_sum = sum(SKILLS_BONUS.get(s, 0) for s in skills)
    edu_mult  = EDUCATION_MULTIPLIER[education]

    raw_salary = (base + exp_hike + skill_sum) * edu_mult

    if job_type == "Internship":
        raw_salary = raw_salary * 0.30   # internship = ~30% of full-time

    salary_min = int(raw_salary * 0.90)
    salary_max = int(raw_salary * 1.10)
    salary_mid = int(raw_salary)

    st.success("### Estimated Salary Range")

    m1, m2, m3 = st.columns(3)
    m1.metric("Minimum",  f"₹{salary_min:,.0f}")
    m2.metric("Median",   f"₹{salary_mid:,.0f}")
    m3.metric("Maximum",  f"₹{salary_max:,.0f}")

    # ── Breakdown table ──────────────────────────────────────────────────────
    st.markdown("#### Salary Breakdown")
    breakdown = pd.DataFrame({
        "Component":  ["Base Salary", "Experience Bonus", "Skills Bonus", "Education Multiplier", "Job Type Factor"],
        "Value (₹)":  [
            f"₹{base:,.0f}",
            f"₹{exp_hike:,.0f}",
            f"₹{skill_sum:,.0f}",
            f"× {edu_mult:.2f}",
            "× 0.30" if job_type == "Internship" else "× 1.00",
        ],
    })
    st.dataframe(breakdown, use_container_width=True, hide_index=True)

    # ── City comparison bar chart ─────────────────────────────────────────────
    st.markdown("#### How your salary compares across cities")
    city_salaries = {}
    for city, city_base in SALARY_DATA[job_title].items():
        city_sal = (city_base + exp_hike + skill_sum) * edu_mult
        if job_type == "Internship":
            city_sal *= 0.30
        city_salaries[city] = int(city_sal)

    city_df = (
        pd.DataFrame.from_dict(city_salaries, orient="index", columns=["Salary"])
        .sort_values("Salary", ascending=True)
    )
    city_df["Salary_L"] = (city_df["Salary"] / 100000).round(1)
    city_df["City"] = city_df.index

    # highlight selected city
    city_df["Color"] = city_df["City"].apply(
        lambda c: "#378ADD" if c == location else "#B5D4F4"
    )

    st.bar_chart(
        city_df.set_index("City")["Salary"],
        use_container_width=True,
        color="#378ADD",
    )
    st.caption(f"Blue = selected city ({location}). Values in ₹.")

    # ── Top skills advice ────────────────────────────────────────────────────
    st.markdown("#### Skills that would increase your salary the most")
    missing = {k: v for k, v in SKILLS_BONUS.items() if k not in skills}
    top_missing = sorted(missing.items(), key=lambda x: x[1], reverse=True)[:5]
    tips_df = pd.DataFrame(top_missing, columns=["Skill", "Potential Bonus (₹)"])
    tips_df["Potential Bonus (₹)"] = tips_df["Potential Bonus (₹)"].apply(lambda x: f"₹{x:,.0f}")
    st.dataframe(tips_df, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Disclaimer: Estimates are based on approximate Indian IT market data for 2026. Actual offers vary by company, interview performance, and negotiation.")
st.caption("Created by Rohan Gupta")
