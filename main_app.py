import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Best Wishes for Your New Beginning",
    page_icon="🎉",
    layout="wide",
)

# Title and Introduction
st.title("🎉 A Beautiful Journey 🎉")
st.markdown(
    """
    *"Every new beginning comes from some other beginning's end."*  
    As you embark on this exciting chapter, here's a celebration of your journey and a heartfelt wish for a bright future ahead!
    """
)

# Timeline Section
st.subheader("Your Life's Journey 🚀")
timeline_data = {
    "2001": "Born - A star was born! 🌟 (Baby photo below)",
    "2018": "Started B.A. in Accountancy and Finance at Heriot-Watt University, UAE.",
    "2021": "Graduated with distinction and joined The Talent Enterprise, Dubai.",
    "2023": "Embarked on a Master of Science in Data Science at Indiana University Bloomington.",
    "2024": "Joined ADM as a Machine Learning Intern (Generative AI Team)."
}

for year, event in timeline_data.items():
    with st.expander(f"**{year}**"):
        st.write(event)
        if year == "2001":
            st.image("bachpan.jpg", caption="Baby Photo", use_container_width=True)

# Family Photos and Messages Section
st.subheader("With Love from Your Family ❤️")
col1, col2, col3 = st.columns(3)

# Predefined messages for each family member
mom_placeholder = """Dear Yukta,
I am so proud of the woman you've become. Your dedication and hard work inspire me every day. May this new chapter bring you all the success and happiness you deserve.
Love, Mom ❤️"""

dad_placeholder = """Dear Yukta,
messgae!
Love, Dad 🌟"""

sister_placeholder = """Dear Di,
"Message here"!
Love, Your Sister 💕"""

with col1:
    st.image("maabaap.jpg", caption="Mom", use_container_width=True)
    mom_message = st.text_area(
        "Message from Mom 💝",
        value=mom_placeholder,
        height=200,
        key="mom_message"
    )

with col2:
    st.image("florida.jpg", caption="Dad", use_container_width=True)
    dad_message = st.text_area(
        "Message from Dad 💝",
        value=dad_placeholder,
        height=200,
        key="dad_message"
    )

with col3:
    st.image("behen.jpg", caption="Sister", use_container_width=True)
    sister_message = st.text_area(
        "Message from Sister 💝",
        value=sister_placeholder,
        height=200,
        key="sister_message"
    )

st.markdown("Your family's unwavering support has shaped your journey, and they are cheering you on every step of the way!")

# Final Message
st.subheader("A Heartfelt Wish 💌")
st.markdown(
    """
    Dear Yukta Sanjay Muthreja,
    
    Congratulations on joining ADM! Your journey so far has been extraordinary, and this new role is another feather in your cap.  
    May this chapter be filled with innovation, growth, and happiness. Wishing you all the success in the world as you continue to inspire everyone around you.
    
    **All the best, always!** 🌟  
    — Your Loved Ones  
    """
)
