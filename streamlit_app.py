import streamlit as st
from datetime import date, timedelta

st.set_page_config(
    page_title="ExploreAmore",
    page_icon="🌴",
    layout="centered"
)

# ---------- STYLE ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #fffaf6 0%, #ffffff 45%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 720px;
    }

    .brand {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .tagline {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-top: 0;
        margin-bottom: 28px;
    }

    .hero {
        padding: 24px;
        border-radius: 22px;
        background: white;
        box-shadow: 0 8px 30px rgba(0,0,0,0.07);
        margin-bottom: 22px;
    }

    .feature {
        padding: 14px;
        border-radius: 16px;
        background: #f7f7f7;
        margin: 8px 0;
        font-size: 16px;
    }

    .promise {
        padding: 20px;
        border-radius: 20px;
        background: #fff3ea;
        margin-top: 25px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 14px;
        height: 52px;
        font-weight: 700;
        font-size: 17px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown('<div class="brand">ExploreAmore 🌴</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="tagline">Holidays designed around your whole family.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero">
<h2>Your holiday. Their adventure. ❤️</h2>

<p>
Complete family package holidays created for families with
disabled and additional-needs children.
</p>

<p>
Flights, accommodation, transfers, catering, personalised activities
and dedicated support — brought together in one holiday.
</p>
</div>
""", unsafe_allow_html=True)


# ---------- HOLIDAY SEARCH ----------
st.subheader("✈️ Build your family holiday")

departure = st.selectbox(
    "Flying from",
    [
        "Manchester",
        "Liverpool",
        "Birmingham",
        "London Gatwick",
        "London Stansted",
        "Bristol",
        "Newcastle"
    ]
)

destination = st.selectbox(
    "Where would you love to go?",
    [
        "Rhodes, Greece 🇬🇷",
        "Majorca, Spain 🇪🇸",
        "Tenerife, Spain 🇪🇸",
        "Algarve, Portugal 🇵🇹",
        "Cyprus 🇨🇾",
        "Turkey 🇹🇷"
    ]
)

arrival = st.date_input(
    "When?",
    value=date.today() + timedelta(days=60),
    min_value=date.today()
)

nights = st.selectbox(
    "How many nights?",
    [5, 7, 10, 14],
    index=1
)

col1, col2 = st.columns(2)

with col1:
    adults = st.number_input(
        "Adults",
        min_value=1,
        max_value=6,
        value=1
    )

with col2:
    children = st.number_input(
        "Children",
        min_value=1,
        max_value=6,
        value=1
    )


# ---------- SUPPORT ----------
st.subheader("❤️ Tell us what your family needs")

support = st.multiselect(
    "What support would make this holiday easier?",
    [
        "Autism-friendly support",
        "Sensory-friendly activities",
        "Mobility / accessibility support",
        "1-to-1 activity support",
        "Communication support",
        "Dietary requirements",
        "Quiet spaces",
        "Parent respite time"
    ]
)

interests = st.text_area(
    "Tell us a little about your child",
    placeholder=(
        "For example: Loves swimming and dinosaurs, prefers quiet places, "
        "doesn't like sudden changes..."
    )
)


# ---------- BUILD BUTTON ----------
if st.button("✨ Build our holiday"):
    st.success("Your personalised holiday is being created ❤️")

    st.markdown("## 🌴 Your ExploreAmore Package")

    st.write(f"✈️ **Return flights:** {departure} → {destination}")
    st.write(f"🏨 **Stay:** {nights} nights family accommodation")
    st.write("🚐 **Airport transfers included**")
    st.write("🍳 **Breakfast included**")
    st.write("🎨 **Personalised activities for your child**")
    st.write("❤️ **Dedicated family support & parent respite sessions**")

    if support:
        st.write("### Your selected support")
        for item in support:
            st.write(f"✓ {item}")

    st.info(
        "Next we'll match your family with suitable accommodation, "
        "flights and a personalised activity plan."
    )


# ---------- FEATURES ----------
st.markdown("---")
st.subheader("Everything taken care of")

st.markdown("""
<div class="feature">✈️ Flights</div>
<div class="feature">🏨 Family-friendly accommodation</div>
<div class="feature">🚐 Airport transfers</div>
<div class="feature">🍳 Breakfast & catering</div>
<div class="feature">❤️ Dedicated child support</div>
<div class="feature">🎨 Personalised activities</div>
<div class="feature">👨‍👩‍👧 Family experiences</div>
<div class="feature">🌅 Time for parents to relax and explore</div>
""", unsafe_allow_html=True)


# ---------- MESSAGE ----------
st.markdown("""
<div class="promise">
<h3>Built around your family ❤️</h3>

<p>
No two children are the same, so no two ExploreAmore holidays
need to be the same.
</p>

<p>
We learn what makes your child happy, comfortable and confident,
then help create a holiday around them — giving the whole family
the chance to enjoy being away.
</p>
</div>
""", unsafe_allow_html=True)

st.caption("ExploreAmore • Supported family holidays")
