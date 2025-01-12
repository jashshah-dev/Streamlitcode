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

# Initialize state for video visibility
if 'show_video' not in st.session_state:
    st.session_state.show_video = False

# Video Section with Toggle Button
st.subheader("📽️ Memory Lane")
if st.button("Watch Graduation Archive 🎓"):
    st.session_state.show_video = not st.session_state.show_video

if st.session_state.show_video:
    video_file = open('graduation_memories.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("*Cherishing these beautiful memories...*")

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
mom_placeholder = """My sweet Yukta,
You will always be my little girl, no matter how big you grow. I’m so proud of the kindness, strength, and determination you carry in your heart. Keep spreading your light and love wherever you go. My blessings are always with you. Love, Mom. ❤️"""

dad_placeholder = """My dearest Cookie,
You’ve always been the sunshine of our home, filling it with laughter and joy. Watching you grow into the wonderful person you are fills me with pride. Keep chasing your dreams with that bright smile of yours – the world is yours to conquer! Love you endlessly, Dad.
 🌟"""

sister_placeholder = """Hey baby sis,
You’re the spark of our family and my favorite partner-in-crime! I’m so proud of everything you’ve achieved and the amazing person you’re becoming. Keep reaching for the stars, and know I’m always here cheering you on. Love you tons, Your Didi. 💕"""

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
