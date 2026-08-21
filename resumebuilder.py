import streamlit as st


# PAGE SETTINGS
st.set_page_config(page_title="Resume Builder By Tanmay", page_icon="📄", layout="centered")

st.title("📄 resume Builder")
st.caption("Fill in the sections below using the dropdowns and checkboxes.")

# ------------------------------------------------------------------
# READY-MADE OPTIONS (feel free to add more items to these lists)
# ------------------------------------------------------------------
DEGREE_OPTIONS = [
    "High School", "Diploma", "B.Tech / B.E.", "B.Sc.", "B.Com",
    "B.A.", "M.Tech / M.E.", "M.Sc.", "MBA", "M.A.", "Ph.D.", "Other"
]

SKILL_OPTIONS = [
    "Python", "JavaScript", "Java", "C++", "SQL", "React",
    "Data Analysis", "Excel", "Communication", "Public Speaking",
    "Project Management", "Git/GitHub", "Machine Learning",
    "Cloud (AWS/Azure)", "UI/UX Design", "Problem Solving",
]

HABIT_OPTIONS = [
    "Daily coding practice", "Reads tech articles weekly", "Early riser",
    "Time management", "Continuous learner", "Team collaborator",
    "Goal journaling", "Regular exercise", "Mentors others", "Note-taking system",
]

SHORT_TERM_GOALS = [
    "Land an internship", "Get an entry-level job", "Switch career fields",
    "Earn a certification", "Build a portfolio project", "Other",
]

LONG_TERM_GOALS = [
    "Become a senior specialist", "Lead a team", "Start my own company",
    "Work abroad", "Move into management", "Become an expert in my field", "Other",
]

ACHIEVEMENT_TYPES = [
    "Certification", "Award", "Project", "Competition", "Publication", "Internship", "Other",
]

YEARS = list(range(2027, 2000, -1))  # dropdown of years, newest first


# ------------------------------------------------------------------
# SECTION 1: PROFILE
# ------------------------------------------------------------------
st.header("1. Profile")

name = st.text_input("Full Name", value="Tanmay Deshmukh")
title = st.text_input("Title / Field", value="Electronics and Telecommunication")
email = st.text_input("Email", value="tanmay@example.com")
phone = st.text_input("Phone", value="9404874531")
location = st.text_input("Location", value="wadsa")
linkedin = st.text_input("LinkedIn (optional)", value="")


# ------------------------------------------------------------------
# SECTION 2: EDUCATION
# ------------------------------------------------------------------
st.header("2. Education")

degree = st.selectbox("Degree", DEGREE_OPTIONS)
field_of_study = st.text_input("Field of Study", value="Electronics and Telecommunication Engineering")
institution = st.text_input("College / School Name", value="YCCE")

col1, col2 = st.columns(2)
with col1:
    start_year = st.selectbox("Start Year", YEARS, index=YEARS.index(2022) if 2022 in YEARS else 0)
with col2:
    end_year = st.selectbox("End Year (or expected)", YEARS, index=YEARS.index(2026) if 2026 in YEARS else 0)

score_type = st.radio("Score Type", ["CGPA", "Percentage", "GPA"], horizontal=True)
score = st.text_input("Score", value="")


# ------------------------------------------------------------------
# SECTION 3: SKILLS AND HABITS
# ------------------------------------------------------------------
st.header("3. Skills & Habits")

skills = st.multiselect("Select your skills", SKILL_OPTIONS)
extra_skill = st.text_input("Add a skill not in the list (optional)")
if extra_skill:
    skills.append(extra_skill)

habits = st.multiselect("Select your habits", HABIT_OPTIONS)
extra_habit = st.text_input("Add a habit not in the list (optional)")
if extra_habit:
    habits.append(extra_habit)


# ------------------------------------------------------------------
# SECTION 4: GOALS
# ------------------------------------------------------------------
st.header("4. Goals")

short_term_goal = st.selectbox("Short-term Goal", SHORT_TERM_GOALS)
short_term_detail = st.text_area("Short-term Goal Detail (optional)", height=70)

long_term_goal = st.selectbox("Long-term Goal", LONG_TERM_GOALS)
long_term_detail = st.text_area("Long-term Goal Detail (optional)", height=70)


# ------------------------------------------------------------------
# SECTION 5: ACHIEVEMENTS
# ------------------------------------------------------------------
st.header("5. Achievements")

achievement_type = st.selectbox("Achievement Type", ACHIEVEMENT_TYPES)
achievement_title = st.text_input("Achievement Title", value="")
achievement_year = st.selectbox("Achievement Year", YEARS, key="ach_year")
achievement_desc = st.text_area("Description (optional)", height=70)


# ------------------------------------------------------------------
# PREVIEW SECTION (shows everything you entered above)
# ------------------------------------------------------------------
st.divider()
st.header("👀 Preview")

if st.button("Generate My Dossier"):

    st.subheader(name)
    st.write(f"**{title}**")
    st.write(f"{email}  |  {phone}  |  {location}  |  {linkedin}")

    st.markdown("### 🎓 Education")
    st.write(f"**{degree}** in {field_of_study}")
    st.write(f"{institution}  ({start_year} - {end_year})")
    st.write(f"{score_type}: {score}")

    st.markdown("### 💡 Skills")
    if skills:
        st.write(", ".join(skills))
    else:
        st.write("No skills selected yet.")

    st.markdown("### 🌱 Habits")
    if habits:
        st.write(", ".join(habits))
    else:
        st.write("No habits selected yet.")

    st.markdown("### 🎯 Goals")
    st.write(f"**Short-term:** {short_term_goal} - {short_term_detail}")
    st.write(f"**Long-term:** {long_term_goal} - {long_term_detail}")

    st.markdown("### 🏆 Achievements")
    st.write(f"**{achievement_title}** ({achievement_type}, {achievement_year})")
    st.write(achievement_desc)

    st.success("This is how your dossier looks! Take a screenshot or add more fields as needed.")