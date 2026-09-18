import streamlit as st
from datetime import date, timedelta

st.set_page_config(
    page_title="ExploreAmore | Rhodes",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "reviews" not in st.session_state:
    st.session_state.reviews = [
        {
            "name": "Sarah & Leo",
            "rating": 5,
            "text": "For once I didn't feel like I had to explain my child everywhere we went. We could just enjoy being a family."
        },
        {
            "name": "Emma",
            "rating": 5,
            "text": "Having activities built around what my son actually enjoys made such a difference."
        },
        {
            "name": "The Williams Family",
            "rating": 5,
            "text": "Rhodes was beautiful and having some proper parent time made the holiday feel like a holiday for all of us."
        }
    ]

if "enquiry_sent" not in st.session_state:
    st.session_state.enquiry_sent = False


# =========================================================
# DESIGN
# =========================================================

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background:
        radial-gradient(circle at 90% 0%, #dff8f5 0%, transparent 28%),
        linear-gradient(180deg, #fffdf8 0%, #ffffff 45%, #f7fbfa 100%);
    color: #173536;
}

.block-container {
    max-width: 1050px;
    padding-top: 1.2rem;
    padding-bottom: 7rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: rgba(255,255,255,0.82) !important;
}

/* ---------- TYPOGRAPHY ---------- */

h1, h2, h3 {
    letter-spacing: -0.02em;
}

.small-label {
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 12px;
    font-weight: 800;
    color: #168b89;
}

.muted {
    color: #647878;
}

/* ---------- BRAND ---------- */

.brand-wrap {
    text-align: center;
    padding: 12px 0 18px 0;
}

.brand {
    font-size: 38px;
    line-height: 1;
    font-weight: 900;
    color: #123f40;
    letter-spacing: -0.05em;
}

.brand span {
    color: #18a6a2;
}

.brand-sub {
    margin-top: 7px;
    font-size: 13px;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #6d8584;
    font-weight: 700;
}

/* ---------- HERO ---------- */

.hero {
    min-height: 470px;
    border-radius: 32px;
    padding: 46px 38px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    color: white;
    background:
        linear-gradient(
            180deg,
            rgba(4,30,34,0.08) 0%,
            rgba(4,30,34,0.22) 40%,
            rgba(4,30,34,0.86) 100%
        ),
        url("https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1600&q=85");
    background-size: cover;
    background-position: center;
    box-shadow: 0 18px 50px rgba(18,63,64,0.18);
}

.hero-pill {
    display: inline-block;
    width: fit-content;
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(8px);
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 13px;
}

.hero h1 {
    font-size: 54px;
    max-width: 700px;
    margin: 0;
    line-height: 1.02;
    color: white;
}

.hero p {
    max-width: 650px;
    font-size: 18px;
    margin-top: 15px;
    margin-bottom: 0;
    color: rgba(255,255,255,0.94);
}

/* ---------- CARDS ---------- */

.card {
    background: rgba(255,255,255,0.96);
    border: 1px solid #e8f0ef;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 9px 30px rgba(26,64,65,0.08);
    margin-bottom: 14px;
}

.card-body {
    padding: 19px;
}

.card h3 {
    margin: 0 0 6px 0;
    color: #173f40;
}

.card p {
    color: #637978;
}

.villa-img {
    width: 100%;
    height: 215px;
    object-fit: cover;
}

.price {
    font-size: 25px;
    font-weight: 900;
    color: #123f40;
}

.tag {
    display: inline-block;
    margin: 3px 3px 3px 0;
    padding: 6px 10px;
    border-radius: 999px;
    background: #e9f8f6;
    color: #147c79;
    font-size: 12px;
    font-weight: 800;
}

.deal {
    padding: 22px;
    border-radius: 24px;
    background: linear-gradient(135deg, #173f40, #176b69);
    color: white;
    box-shadow: 0 12px 32px rgba(18,63,64,.18);
    margin-bottom: 16px;
}

.deal h3 {
    color: white;
    margin-bottom: 5px;
}

.deal p {
    color: #e7ffff;
}

/* ---------- SUPPORT ---------- */

.support-box {
    border-radius: 28px;
    padding: 26px;
    background: #fff3e9;
    border: 1px solid #ffe1ca;
    margin: 20px 0;
}

.support-box h2 {
    color: #563e2f;
}

/* ---------- REVIEW ---------- */

.review {
    background: white;
    border-radius: 20px;
    padding: 19px;
    border: 1px solid #e7eeee;
    margin-bottom: 12px;
}

.stars {
    color: #d99a00;
    font-size: 18px;
}

/* ---------- BUTTONS ---------- */

div.stButton > button {
    width: 100%;
    border-radius: 14px;
    min-height: 48px;
    font-weight: 800;
    border: 1px solid #dce9e8;
}

div.stButton > button[kind="primary"] {
    background: #123f40;
    color: white;
}

/* ---------- NAV ---------- */

.nav-title {
    font-size: 12px;
    color: #6c8180;
    text-align: center;
    margin-bottom: 4px;
}

/* ---------- MOBILE ---------- */

@media (max-width: 700px) {

    .block-container {
        padding-left: 15px;
        padding-right: 15px;
        padding-top: .8rem;
    }

    .brand {
        font-size: 32px;
    }

    .hero {
        min-height: 440px;
        padding: 28px 22px;
        border-radius: 25px;
    }

    .hero h1 {
        font-size: 39px;
    }

    .hero p {
        font-size: 16px;
    }

    .villa-img {
        height: 190px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================

def navigate(page):
    st.session_state.page = page


def header():
    st.markdown("""
    <div class="brand-wrap">
        <div class="brand">Explore<span>Amore</span></div>
        <div class="brand-sub">Rhodes • Holidays built around your family</div>
    </div>
    """, unsafe_allow_html=True)


def navigation():
    st.markdown("---")
    st.markdown('<div class="nav-title">EXPLORE</div>', unsafe_allow_html=True)

    cols = st.columns(5)

    with cols[0]:
        if st.button("🏠\nHome"):
            navigate("Home")
            st.rerun()

    with cols[1]:
        if st.button("🏡\nVillas"):
            navigate("Villas")
            st.rerun()

    with cols[2]:
        if st.button("❤️\nFamily"):
            navigate("Family")
            st.rerun()

    with cols[3]:
        if st.button("⭐\nCommunity"):
            navigate("Community")
            st.rerun()

    with cols[4]:
        if st.button("🔐\nNicola"):
            navigate("Admin")
            st.rerun()


# =========================================================
# DATA
# =========================================================

villas = [
    {
        "name": "Villa Amore",
        "area": "Lindos",
        "image": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?auto=format&fit=crop&w=1200&q=85",
        "price": "£1,895",
        "sleeps": "Sleeps 6",
        "pool": "Private pool",
        "feature": "Quiet setting",
        "description": "A peaceful family villa with private outdoor space and room to reset away from busy resort areas."
    },
    {
        "name": "Aegean Family Retreat",
        "area": "Pefkos",
        "image": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=85",
        "price": "£2,240",
        "sleeps": "Sleeps 8",
        "pool": "Private pool",
        "feature": "Family favourite",
        "description": "Spacious accommodation close to the coast with flexible spaces for play, downtime and family evenings."
    },
    {
        "name": "Blue Haven",
        "area": "Kolymbia",
        "image": "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&w=1200&q=85",
        "price": "£1,675",
        "sleeps": "Sleeps 5",
        "pool": "Pool access",
        "feature": "Calmer resort",
        "description": "A relaxed base for families wanting beaches, activities and quieter moments within easy reach."
    }
]


# =========================================================
# HOME
# =========================================================

def home_page():

    st.markdown("""
    <div class="hero">
        <div class="hero-pill">☀️ RHODES • GREECE</div>
        <h1>A holiday for the whole family.</h1>
        <p>
        Beautiful Rhodes stays, flights, transfers and experiences —
        with personalised support built around your child's individual needs.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("✨ Build our Rhodes holiday", type="primary"):
        navigate("Family")
        st.rerun()

    st.markdown("### Everything in one holiday")

    c1, c2 = st.columns(2)

    with c1:
        st.info("✈️ **Flights**\n\nFind suitable travel from UK airports.")
        st.info("🏡 **Hand-picked stays**\n\nFamily villas and accommodation across Rhodes.")
        st.info("🎨 **Personalised activities**\n\nBuilt around interests, comfort and confidence.")

    with c2:
        st.info("🚐 **Transfers**\n\nMake arrival and departure easier.")
        st.info("🍳 **Food & catering**\n\nBreakfast and dietary preferences planned ahead.")
        st.info("❤️ **Parent time**\n\nSupported sessions giving parents space to relax.")

    st.markdown("""
    <div class="support-box">
        <div class="small-label">THE EXPLOREAMORE DIFFERENCE</div>
        <h2>We get to know the child, not just the booking.</h2>
        <p>
        Every autistic child is different. Families can tell us about
        communication, routines, sensory preferences, favourite activities,
        food, transitions and what helps their child feel comfortable.
        </p>
        <p>
        That information helps the human ExploreAmore team shape activities
        and the holiday experience around the individual family.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🔥 Current Rhodes deals")

    st.markdown("""
    <div class="deal">
        <div class="small-label" style="color:#9fe5df;">FEATURED FAMILY ESCAPE</div>
        <h3>7 nights • Lindos</h3>
        <p>Villa stay + transfers + breakfast welcome pack + personalised family activity plan.</p>
        <b>From £1,895 per family*</b>
    </div>
    """, unsafe_allow_html=True)

    if st.button("See Rhodes villas →"):
        navigate("Villas")
        st.rerun()

    st.caption("*Demo pricing while ExploreAmore is being developed. Live supplier pricing will be connected later.")


# =========================================================
# VILLAS
# =========================================================

def villas_page():

    st.markdown('<div class="small-label">STAY YOUR WAY</div>', unsafe_allow_html=True)
    st.title("Rhodes villas 🏡")

    st.write(
        "Explore family stays across Rhodes. Nicola can eventually add, "
        "remove and update these from her own dashboard."
    )

    area = st.selectbox(
        "Area",
        ["All Rhodes", "Lindos", "Pefkos", "Kolymbia"]
    )

    for villa in villas:

        if area != "All Rhodes" and villa["area"] != area:
            continue

        st.markdown(f"""
        <div class="card">
            <img class="villa-img" src="{villa['image']}">
            <div class="card-body">
                <div class="small-label">{villa['area'].upper()} • RHODES</div>
                <h3>{villa['name']}</h3>
                <p>{villa['description']}</p>

                <span class="tag">👨‍👩‍👧 {villa['sleeps']}</span>
                <span class="tag">🏊 {villa['pool']}</span>
                <span class="tag">❤️ {villa['feature']}</span>

                <p class="price">From {villa['price']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "Check availability",
                key=f"availability_{villa['name']}"
            ):
                st.session_state.selected_villa = villa["name"]
                navigate("Availability")
                st.rerun()

        with col2:
            if st.button(
                "Ask about this villa",
                key=f"ask_{villa['name']}"
            ):
                st.session_state.selected_villa = villa["name"]
                navigate("Enquiry")
                st.rerun()


# =========================================================
# AVAILABILITY
# =========================================================

def availability_page():

    villa = st.session_state.get("selected_villa", "ExploreAmore Villa")

    st.markdown('<div class="small-label">PLAN YOUR STAY</div>', unsafe_allow_html=True)
    st.title("Availability 📅")
    st.subheader(villa)

    st.info(
        "This is the booking-calendar experience. "
        "Live villa inventory will be connected to a booking database/supplier later."
    )

    check_in = st.date_input(
        "Check in",
        value=date.today() + timedelta(days=60),
        min_value=date.today()
    )

    nights = st.selectbox(
        "Nights",
        [5, 7, 10, 14],
        index=1
    )

    adults = st.number_input(
        "Adults",
        min_value=1,
        max_value=8,
        value=2
    )

    children = st.number_input(
        "Children",
        min_value=1,
        max_value=6,
        value=1
    )

    check_out = check_in + timedelta(days=nights)

    st.success(
        f"Selected stay: {check_in.strftime('%d %b %Y')} → "
        f"{check_out.strftime('%d %b %Y')} • {nights} nights"
    )

    if st.button("Continue with this holiday", type="primary"):
        st.session_state.travel_dates = (
            check_in,
            check_out,
            adults,
            children
        )
        navigate("Family")
        st.rerun()


# =========================================================
# FAMILY PROFILE
# =========================================================

def family_page():

    st.markdown('<div class="small-label">YOUR FAMILY</div>', unsafe_allow_html=True)
    st.title("Tell us about your child ❤️")

    st.write(
        "Not a medical form. Just the things that can help us understand "
        "what makes your child comfortable, confident and happy."
    )

    child_name = st.text_input(
        "Child's first name or nickname"
    )

    age = st.number_input(
        "Age",
        min_value=2,
        max_value=17,
        value=8
    )

    communication = st.multiselect(
        "Communication",
        [
            "Speaks independently",
            "Uses short phrases",
            "Non-speaking",
            "AAC / communication device",
            "Visual communication helps",
            "Needs extra processing time"
        ]
    )

    sensory = st.multiselect(
        "Sensory preferences",
        [
            "Prefers quieter places",
            "Sensitive to loud noise",
            "Sensitive to bright lights",
            "Doesn't like large crowds",
            "Needs movement / active play",
            "Benefits from sensory breaks",
            "No particular sensory needs"
        ]
    )

    interests = st.text_area(
        "What do they LOVE?",
        placeholder="Swimming, dinosaurs, football, animals, drawing, gaming..."
    )

    difficult = st.text_area(
        "Anything that can make things difficult?",
        placeholder="Unexpected changes, queues, loud music, unfamiliar food..."
    )

    food = st.text_area(
        "Food, allergies or eating preferences",
        placeholder="Favourite breakfast, safe foods, allergies, textures to avoid..."
    )

    support = st.multiselect(
        "What would help your family?",
        [
            "Supported activity sessions",
            "1-to-1 support",
            "Quiet activities",
            "Visual holiday schedule",
            "Help with transitions",
            "Parent respite time",
            "Family activities together",
            "Flexible meal planning"
        ]
    )

    parent_time = st.slider(
        "How much parent free-time would you ideally like during the week?",
        min_value=0,
        max_value=20,
        value=6,
        step=1
    )

    if st.button("✨ Create our holiday profile", type="primary"):

        st.session_state.family_profile = {
            "name": child_name or "Your child",
            "age": age,
            "communication": communication,
            "sensory": sensory,
            "interests": interests,
            "difficult": difficult,
            "food": food,
            "support": support,
            "parent_time": parent_time
        }

        navigate("Plan")
        st.rerun()


# =========================================================
# PERSONALISED PLAN
# =========================================================

def plan_page():

    profile = st.session_state.get("family_profile")

    if not profile:
        st.warning("Create your family profile first.")
        if st.button("Create profile"):
            navigate("Family")
            st.rerun()
        return

    st.markdown('<div class="small-label">MADE FOR YOUR FAMILY</div>', unsafe_allow_html=True)
    st.title(f"{profile['name']}'s Rhodes adventure 🌊")

    st.write(
        "This is an example personalised itinerary. "
        "The final plan would be reviewed and adapted with the family."
    )

    st.markdown("""
    ### Day 1 • Arrive gently
    🚐 Private transfer to your accommodation

    🏡 Time to settle in with no planned activities

    🍽️ Familiar food options available

    🌅 Quiet family evening
    """)

    st.markdown("""
    ### Day 2 • Discover & play
    🏊 Morning pool / swimming session

    🎨 Personalised activity session

    ☕ Parent free-time

    👨‍👩‍👧 Family sunset activity
    """)

    st.markdown("""
    ### Day 3 • Explore Rhodes
    🏖️ Flexible beach morning

    ❤️ Supported child activity

    🌴 Parent time to explore, relax or eat out

    🍽️ Family dinner
    """)

    if profile["interests"]:
        st.success(
            f"Activities will be shaped around: {profile['interests']}"
        )

    st.info(
        f"Requested parent free-time: approximately "
        f"{profile['parent_time']} hours across the holiday."
    )

    if st.button("Enquire about this holiday", type="primary"):
        navigate("Enquiry")
        st.rerun()


# =========================================================
# ENQUIRY
# =========================================================

def enquiry_page():

    st.markdown('<div class="small-label">START YOUR HOLIDAY</div>', unsafe_allow_html=True)
    st.title("Talk to ExploreAmore 💬")

    villa = st.session_state.get(
        "selected_villa",
        "Help me choose"
    )

    with st.form("holiday_enquiry"):

        name = st.text_input("Your name")
        email = st.text_input("Email")
        phone = st.text_input("Phone / WhatsApp")

        st.text_input(
            "Villa",
            value=villa
        )

        airport = st.selectbox(
            "Preferred UK airport",
            [
                "Manchester",
                "Liverpool",
                "Birmingham",
                "London Gatwick",
                "London Stansted",
                "Other"
            ]
        )

        message = st.text_area(
            "Anything else you'd like Nicola to know?"
        )

        submitted = st.form_submit_button(
            "Send holiday enquiry",
            type="primary"
        )

        if submitted:

            if not name or not email:
                st.error("Please add your name and email.")
            else:
                st.session_state.enquiry_sent = True
                st.success(
                    "❤️ Enquiry received. In the live version this will "
                    "appear in Nicola's dashboard automatically."
                )


# =========================================================
# COMMUNITY
# =========================================================

def community_page():

    st.markdown('<div class="small-label">REAL FAMILY EXPERIENCES</div>', unsafe_allow_html=True)
    st.title("ExploreAmore Community ⭐")

    st.write(
        "Families can share experiences, tips and recommendations "
        "to help other parents feel more confident about travelling."
    )

    for review in st.session_state.reviews:

        stars = "★" * review["rating"]

        st.markdown(f"""
        <div class="review">
            <div class="stars">{stars}</div>
            <h3>{review['name']}</h3>
            <p>“{review['text']}”</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Leave a review")

    with st.form("review_form"):

        review_name = st.text_input(
            "Name / family name"
        )

        rating = st.select_slider(
            "Rating",
            options=[1, 2, 3, 4, 5],
            value=5
        )

        review_text = st.text_area(
            "Share your experience"
        )

        add_review = st.form_submit_button(
            "Post review"
        )

        if add_review and review_name and review_text:

            st.session_state.reviews.insert(
                0,
                {
                    "name": review_name,
                    "rating": rating,
                    "text": review_text
                }
            )

            st.success("Review added ❤️")
            st.rerun()


# =========================================================
# NICOLA ADMIN
# =========================================================

def admin_page():

    st.markdown('<div class="small-label">BUSINESS AREA</div>', unsafe_allow_html=True)
    st.title("Nicola's Dashboard 🔐")

    st.warning(
        "DEMO ADMIN AREA — we'll add proper secure login and a database "
        "before this is used with real customer information."
    )

    password = st.text_input(
        "Demo password",
        type="password"
    )

    if password != "nicola":

        st.info(
            "For the prototype, enter: nicola"
        )

        return

    st.success("Dashboard unlocked")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🏡 Villas",
            "🔥 Deals",
            "📅 Availability",
            "💬 Enquiries"
        ]
    )

    with tab1:

        st.subheader("Add a villa")

        villa_name = st.text_input(
            "Villa name",
            key="admin_villa_name"
        )

        villa_area = st.selectbox(
            "Area",
            [
                "Lindos",
                "Pefkos",
                "Kolymbia",
                "Faliraki",
                "Rhodes Town",
                "Other"
            ],
            key="admin_villa_area"
        )

        villa_price = st.number_input(
            "From price (£)",
            min_value=0,
            value=1800,
            step=50
        )

        st.text_area(
            "Description",
            key="admin_villa_description"
        )

        if st.button("Add villa"):
            st.success(
                f"{villa_name or 'New villa'} prepared for publishing. "
                "Permanent saving comes when we connect the database."
            )

    with tab2:

        st.subheader("Create a new deal")

        deal_title = st.text_input(
            "Deal title"
        )

        deal_price = st.number_input(
            "Price (£)",
            min_value=0,
            value=1895,
            step=50,
            key="deal_price"
        )

        deal_text = st.text_area(
            "What's included?"
        )

        if st.button("Publish deal"):
            st.success(
                f"{deal_title or 'Deal'} preview created."
            )

    with tab3:

        st.subheader("Villa availability")

        st.date_input(
            "Choose dates",
            value=(
                date.today() + timedelta(days=30),
                date.today() + timedelta(days=37)
            )
        )

        status = st.selectbox(
            "Status",
            [
                "Available",
                "Reserved",
                "Booked",
                "Unavailable"
            ]
        )

        if st.button("Update availability"):
            st.success(
                f"Availability marked as {status} in the demo."
            )

    with tab4:

        st.subheader("Customer enquiries")

        st.info(
            "New enquiries will appear here once we connect "
            "ExploreAmore to its permanent database."
        )


# =========================================================
# APP
# =========================================================

header()

page = st.session_state.page

if page == "Home":
    home_page()

elif page == "Villas":
    villas_page()

elif page == "Availability":
    availability_page()

elif page == "Family":
    family_page()

elif page == "Plan":
    plan_page()

elif page == "Enquiry":
    enquiry_page()

elif page == "Community":
    community_page()

elif page == "Admin":
    admin_page()

navigation()

st.markdown("---")

st.caption(
    "ExploreAmore • Rhodes, Greece 🇬🇷 • "
    "A family holiday concept built around individual needs."
)
