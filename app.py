import streamlit as st

st.set_page_config(page_title="📘 DOCGUIDE - Tamil Nadu Scholarship Finder", layout="centered")

st.title("📘 DOCGUIDE - Tamil Nadu Scholarship Finder")
st.markdown("Fill in your details to see eligible scholarships in Tamil Nadu.")

name = st.text_input("👤 Name")
caste = st.selectbox("🏷️ Caste", ["Adi Dravidar", "Nadar", "Vanniyar", "Chettiar", "Gounder", "Thevar", "Others"])
community = st.selectbox("🆔 Community", ["OC", "BC", "MBC", "SC", "ST", "BCM"])
religion = st.selectbox("☪️ Religion", ["Hindu", "Muslim", "Christian", "Others"])
annual_income = st.number_input("💵 Annual Income (INR)", min_value=0)
first_graduate = st.radio("🎓 First Graduate", ["Yes", "No"])
disability = st.radio("♿ Disability", ["Yes", "No"])

def get_scholarships():
    scholarships = []
    tn_scholarships = [
        {
            "name": "🎓 First Graduate Scholarship",
            "criteria": {"first_graduate": "Yes"},
            "link": "https://tndce.tn.gov.in/Home/scholarship_cms"
        },
        {
            "name": "📜 SC/ST Scholarship",
            "criteria": {"community": ["SC", "ST"]},
            "link": "https://tndce.tn.gov.in/Home/scholarship_cms"
        },
        {
            "name": "🏛️ BC/MBC Scholarship",
            "criteria": {"community": ["BC", "MBC", "BCM"]},
            "link": "https://tndce.tn.gov.in/Home/scholarship_cms"
        },
        {
            "name": "🕌 Minority Scholarship",
            "criteria": {"religion": ["Muslim", "Christian", "Others"]},
            "link": "https://tndce.tn.gov.in/Home/scholarship_cms"
        },
        {
            "name": "♿ Differently Abled Scholarship",
            "criteria": {"disability": "Yes"},
            "link": "https://tndce.tn.gov.in/Home/scholarship_cms"
        },
        {
            "name": "💰 Income-based Scholarship",
            "criteria": {"annual_income": 200000},
            "link": "https://tndce.tn.gov.in/Home/scholarship_cms"
        }
    ]

    for scholarship in tn_scholarships:
        match = True
        for key, value in scholarship["criteria"].items():
            if key == "community" and community not in value:
                match = False
            elif key == "religion" and religion not in value:
                match = False
            elif key == "annual_income" and annual_income > value:
                match = False
            elif key == "first_graduate" and first_graduate != value:
                match = False
            elif key == "disability" and disability != value:
                match = False
        if match:
            scholarships.append(f"[{scholarship['name']}]({scholarship['link']})")

    return scholarships

if st.button("🔍 Find Eligible Scholarships"):
    results = get_scholarships()
    if results:
        st.success("You are eligible for the following scholarships:")
        for item in results:
            st.markdown(f"- {item}")
    else:
        st.warning("❌ No scholarships available for the given criteria.")
