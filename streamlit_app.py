import streamlit as st
import json
import os
from datetime import date, datetime

st.set_page_config(
    page_title="ExploreAmore | Rhodes",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# EXPLOREAMORE
# Rhodes family package holiday platform
# =========================================================

DATA_FILE = "exploreamore_data.json"

DEFAULT_DATA = {
    "packages": [
        {
            "id": 1,
            "title": "Lindos Family Escape",
            "location": "Lindos, Rhodes",
            "nights": 7,
            "departure_airport": "Manchester",
            "start_date": "2027-05-12",
            "end_date": "2027-05-19",
            "villa": "Villa Athena",
            "price": 2450,
            "spaces": 3,
            "flights": True,
            "transfers": True,
            "breakfast": True,
            "support_hours": 20,
            "activities": "Beach morning, sensory-friendly Rhodes experience, family activity day",
            "description": "A complete supported Rhodes holiday designed around the whole family.",
            "image": "https://images.unsplash.com/photo-1530841377377-3ff06c0ca713?auto=format&fit=crop&w=1400&q=80",
            "featured": True,
            "published": True
        }
    ],
    "enquiries": [],
    "reviews": [
        {
            "name": "Demo family",
            "rating": 5,
            "text": "The idea of having the holiday adapted around our child would make travelling feel possible again.",
            "approved": True
        }
    ]
}


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    save_data(DEFAULT_DATA)
    return DEFAULT_DATA.copy()


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if "data" not in st.session_state:
    st.session_state.data = load_data()

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_package" not in st.session_state:
    st.session_state.selected_package = None

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# =========================================================
# DESIGN
# =========================================================

st.markdown("""
<style>

[data-testid="stHeader"] {
    background: rgba(255,255,255,.88);
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 90% 10%, #dff9f6 0, transparent 28%),
        linear-gradient(180deg,#fffdf8 0%,#f7fcfb 100%);
}

.block-container {
    max-width: 1100px;
    padding-top: 1.2rem;
    padding-bottom: 5rem;
}

h1,h2,h3 {
    color:#103f3d;
    letter-spacing:-0.03em;
}

.logo {
    font-size:2.6rem;
    font-weight:900;
    letter-spacing:-.07em;
    color:#103f3d;
    margin-bottom:0;
}

.logo span {
    color:#23aaa5;
}

.eyebrow {
    color:#218e8a;
    font-size:.82rem;
    font-weight:800;
    letter-spacing:.18em;
    text-transform:uppercase;
}

.hero {
    min-height:540px;
    border-radius:34px;
    padding:45px;
    display:flex;
    flex-direction:column;
    justify-content:flex-end;
    color:white;
    background:
        linear-gradient(0deg,rgba(5,35,34,.85),rgba(5,35,34,.05)),
        url("https://images.unsplash.com/photo-1530841377377-3ff06c0ca713?auto=format&fit=crop&w=1600&q=85");
    background-size:cover;
    background-position:center;
    box-shadow:0 20px 60px rgba(12,65,63,.15);
}

.hero h1 {
    color:white;
    font-size:4rem;
    max-width:720px;
    line-height:.98;
    margin-bottom:20px;
}

.hero p {
    font-size:1.2rem;
    max-width:720px;
}

.package-card {
    background:white;
    border:1px solid #dce9e7;
    border-radius:28px;
    padding:22px;
    margin-bottom:20px;
    box-shadow:0 12px 35px rgba(12,65,63,.07);
}

.package-image {
    width:100%;
    height:300px;
    object-fit:cover;
    border-radius:22px;
}

.price {
    font-size:2rem;
    font-weight:900;
    color:#103f3d;
}

.pill {
    display:inline-block;
    padding:7px 12px;
    margin:3px;
    background:#e6f7f5;
    color:#126d69;
    border-radius:999px;
    font-size:.82rem;
    font-weight:700;
}

.notice {
    background:#fff3e7;
    border:1px solid #ffd9b5;
    padding:18px;
    border-radius:18px;
}

.admin-box {
    background:#103f3d;
    color:white;
    padding:25px;
    border-radius:24px;
}

div.stButton > button {
    border-radius:999px;
    min-height:48px;
    font-weight:750;
    border:1px solid #cddfdd;
}

div.stButton > button[kind="primary"] {
    background:#0f5b57;
    border-color:#0f5b57;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def get_package(package_id):
    for package in st.session_state.data["packages"]:
        if package["id"] == package_id:
            return package
    return None


def money(value):
    return f"£{int(value):,}"


def package_badges(p):
    badges = []

    if p.get("flights"):
        badges.append("✈️ Flights")
    if p.get("transfers"):
        badges.append("🚐 Transfers")
    if p.get("breakfast"):
        badges.append("🍳 Breakfast")

    badges.append(f"❤️ {p.get('support_hours', 0)} hrs support")
    return badges


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="logo">Explore<span>Amore</span></div>',
    unsafe_allow_html=True
)

st.caption("RHODES • FAMILY HOLIDAYS BUILT AROUND YOUR FAMILY")

nav_cols = st.columns(5)

with nav_cols[0]:
    if st.button("🏠 Home", use_container_width=True):
        go("Home")

with nav_cols[1]:
    if st.button("☀️ Packages", use_container_width=True):
        go("Packages")

with nav_cols[2]:
    if st.button("🏡 Villas", use_container_width=True):
        go("Villas")

with nav_cols[3]:
    if st.button("⭐ Community", use_container_width=True):
        go("Community")

with nav_cols[4]:
    if st.button("🔐 Nicola", use_container_width=True):
        go("Admin")

st.markdown("---")


# =========================================================
# HOME
# =========================================================

def home_page():

    st.markdown("""
    <div class="hero">
        <div class="eyebrow" style="color:#9ef2eb;">RHODES • GREECE</div>
        <h1>A holiday for the whole family.</h1>
        <p>
        Complete Rhodes package holidays with flights, accommodation,
        transfers and personalised family support — organised together,
        not left for parents to piece together themselves.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "✨ Explore Rhodes packages",
        type="primary",
        use_container_width=True
    ):
        go("Packages")

    st.write("")
    st.header("Everything organised together")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("✈️ Complete travel")
        st.write(
            "Selected packages can include return flights from the UK, "
            "Rhodes accommodation and airport transfers."
        )

    with c2:
        st.subheader("❤️ Individual support")
        st.write(
            "Families tell ExploreAmore about routines, communication, "
            "sensory preferences, interests and support requirements."
        )

    with c3:
        st.subheader("🌴 Parent time")
        st.write(
            "Supported sessions and planned activities can give parents "
            "time to relax while their child enjoys their holiday too."
        )

    st.write("")
    st.header("🔥 Current Rhodes packages")

    published = [
        p for p in st.session_state.data["packages"]
        if p.get("published")
    ]

    if not published:
        st.info("New Rhodes packages are being prepared.")

    for p in published[:3]:
        package_preview(p)


# =========================================================
# PACKAGE PREVIEW
# =========================================================

def package_preview(p):

    st.markdown('<div class="package-card">', unsafe_allow_html=True)

    if p.get("image"):
        st.image(p["image"], use_container_width=True)

    if p.get("featured"):
        st.markdown("**✨ FEATURED FAMILY ESCAPE**")

    st.subheader(p["title"])
    st.write(f"📍 {p['location']}")
    st.write(
        f"**{p['nights']} nights • "
        f"{p['start_date']} → {p['end_date']}**"
    )

    st.write(
        f"✈️ Departing **{p['departure_airport']}**  \n"
        f"🏡 **{p['villa']}**"
    )

    for badge in package_badges(p):
        st.markdown(
            f'<span class="pill">{badge}</span>',
            unsafe_allow_html=True
        )

    st.write("")
    st.markdown(
        f'<div class="price">From {money(p["price"])} per family*</div>',
        unsafe_allow_html=True
    )

    st.caption(f"Current availability: {p['spaces']} package(s)")

    if st.button(
        "View complete package →",
        key=f"view_{p['id']}",
        use_container_width=True
    ):
        st.session_state.selected_package = p["id"]
        go("Package")

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PACKAGES
# =========================================================

def packages_page():

    st.markdown(
        '<div class="eyebrow">EXPLOREAMORE HOLIDAYS</div>',
        unsafe_allow_html=True
    )

    st.title("Rhodes package holidays")

    st.write(
        "These are complete ExploreAmore holiday packages. "
        "You choose the package — we organise the components shown."
    )

    published = [
        p for p in st.session_state.data["packages"]
        if p.get("published")
    ]

    if not published:
        st.info("There are currently no published packages.")

    for p in published:
        package_preview(p)


# =========================================================
# PACKAGE DETAILS
# =========================================================

def package_page():

    p = get_package(st.session_state.selected_package)

    if not p:
        st.warning("Package not found.")
        return

    if st.button("← Back to packages"):
        go("Packages")

    if p.get("image"):
        st.image(p["image"], use_container_width=True)

    st.markdown(
        '<div class="eyebrow">COMPLETE RHODES PACKAGE</div>',
        unsafe_allow_html=True
    )

    st.title(p["title"])
    st.subheader(f"📍 {p['location']}")

    st.write(p["description"])

    a, b, c = st.columns(3)

    with a:
        st.metric("Nights", p["nights"])

    with b:
        st.metric("From", money(p["price"]))

    with c:
        st.metric("Available", p["spaces"])

    st.subheader("Your holiday")

    st.write(f"📅 **{p['start_date']} → {p['end_date']}**")
    st.write(f"✈️ Departure airport: **{p['departure_airport']}**")
    st.write(f"🏡 Accommodation: **{p['villa']}**")

    if p.get("flights"):
        st.write("✅ Return flights included")

    if p.get("transfers"):
        st.write("✅ Rhodes airport transfers included")

    if p.get("breakfast"):
        st.write("✅ Breakfast / welcome catering included")

    st.write(
        f"❤️ **{p.get('support_hours', 0)} hours** "
        "of planned child/family support"
    )

    st.write(f"🎨 **Activities:** {p.get('activities', '')}")

    st.markdown("---")

    if p["spaces"] > 0:
        if st.button(
            "❤️ Enquire about this holiday",
            type="primary",
            use_container_width=True
        ):
            go("Enquiry")
    else:
        st.error("This package is currently sold out.")


# =========================================================
# ENQUIRY
# =========================================================

def enquiry_page():

    p = get_package(st.session_state.selected_package)

    if not p:
        st.warning("Please choose a package first.")
        return

    st.markdown(
        '<div class="eyebrow">START YOUR HOLIDAY</div>',
        unsafe_allow_html=True
    )

    st.title(p["title"])
    st.write(
        "Tell ExploreAmore about your family. "
        "This is an enquiry — no payment is taken here."
    )

    with st.form("holiday_enquiry"):

        name = st.text_input("Parent / carer name")
        email = st.text_input("Email")
        phone = st.text_input("Phone number")

        c1, c2 = st.columns(2)

        with c1:
            adults = st.number_input(
                "Adults", 1, 10, 2
            )

        with c2:
            children = st.number_input(
                "Children", 1, 10, 1
            )

        st.subheader("Tell us about your child / children")

        communication = st.text_area(
            "Communication preferences"
        )

        sensory = st.text_area(
            "Sensory needs or things they prefer to avoid"
        )

        interests = st.text_area(
            "Favourite activities, interests and things they love"
        )

        food = st.text_area(
            "Food preferences / allergies / dietary requirements"
        )

        routine = st.text_area(
            "Routine, transitions or anything that helps them feel comfortable"
        )

        support = st.text_area(
            "What would make this holiday easier for your family?"
        )

        submitted = st.form_submit_button(
            "Send holiday enquiry ❤️",
            type="primary",
            use_container_width=True
        )

        if submitted:

            if not name or not email:
                st.error("Please add your name and email.")

            else:
                enquiry = {
                    "id": int(datetime.now().timestamp()),
                    "created": datetime.now().isoformat(),
                    "package_id": p["id"],
                    "package": p["title"],
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "adults": adults,
                    "children": children,
                    "communication": communication,
                    "sensory": sensory,
                    "interests": interests,
                    "food": food,
                    "routine": routine,
                    "support": support,
                    "status": "New"
                }

                st.session_state.data["enquiries"].append(enquiry)
                save_data(st.session_state.data)

                st.success(
                    "❤️ Enquiry sent. ExploreAmore can now contact "
                    "the family about this package."
                )


# =========================================================
# VILLAS
# =========================================================

def villas_page():

    st.markdown(
        '<div class="eyebrow">WHERE YOU COULD STAY</div>',
        unsafe_allow_html=True
    )

    st.title("Rhodes stays 🏡")

    st.write(
        "Accommodation is attached to ExploreAmore packages rather "
        "than leaving families to build the holiday themselves."
    )

    villas = {}

    for p in st.session_state.data["packages"]:
        if p.get("published"):
            villas[p["villa"]] = p

    for villa, p in villas.items():

        st.markdown('<div class="package-card">', unsafe_allow_html=True)

        if p.get("image"):
            st.image(p["image"], use_container_width=True)

        st.subheader(villa)
        st.write(f"📍 {p['location']}")
        st.write(f"Available through **{p['title']}**")

        if st.button(
            f"View {p['title']}",
            key=f"villa_{p['id']}"
        ):
            st.session_state.selected_package = p["id"]
            go("Package")

        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# COMMUNITY
# =========================================================

def community_page():

    st.markdown(
        '<div class="eyebrow">EXPLOREAMORE COMMUNITY</div>',
        unsafe_allow_html=True
    )

    st.title("Families helping families ⭐")

    approved = [
        r for r in st.session_state.data["reviews"]
        if r.get("approved")
    ]

    for review in approved:

        st.markdown('<div class="package-card">', unsafe_allow_html=True)

        st.write("⭐" * int(review["rating"]))
        st.subheader(review["name"])
        st.write(review["text"])

        st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Share your experience")

    with st.form("review_form"):

        name = st.text_input("Your name / family name")
        rating = st.slider("Rating", 1, 5, 5)
        text = st.text_area("Your review")

        if st.form_submit_button("Submit review"):

            if name and text:

                st.session_state.data["reviews"].append({
                    "name": name,
                    "rating": rating,
                    "text": text,
                    "approved": False
                })

                save_data(st.session_state.data)

                st.success(
                    "Thank you ❤️ Your review has been sent "
                    "to ExploreAmore for approval."
                )


# =========================================================
# ADMIN LOGIN
# =========================================================

def admin_login():

    st.markdown(
        '<div class="eyebrow">PRIVATE AREA</div>',
        unsafe_allow_html=True
    )

    st.title("🔐 Nicola's ExploreAmore")

    st.write(
        "This area controls the holidays customers see."
    )

    password = st.text_input(
        "Admin password",
        type="password"
    )

    if st.button(
        "Open dashboard",
        type="primary",
        use_container_width=True
    ):

        # DEMO PASSWORD - change later
        if password == "Rhodes2027!":
            st.session_state.admin_logged_in = True
            st.rerun()
        else:
            st.error("Incorrect password.")


# =========================================================
# ADMIN
# =========================================================

def admin_page():

    if not st.session_state.admin_logged_in:
        admin_login()
        return

    st.markdown(
        '<div class="eyebrow">EXPLOREAMORE CONTROL CENTRE</div>',
        unsafe_allow_html=True
    )

    st.title("Nicola's Dashboard 🔐")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Packages",
        len(st.session_state.data["packages"])
    )

    c2.metric(
        "New enquiries",
        len([
            e for e in st.session_state.data["enquiries"]
            if e.get("status") == "New"
        ])
    )

    c3.metric(
        "Reviews waiting",
        len([
            r for r in st.session_state.data["reviews"]
            if not r.get("approved")
        ])
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "☀️ Packages",
        "➕ New package",
        "📩 Enquiries",
        "⭐ Reviews"
    ])


    # -----------------------------------------------------
    # EXISTING PACKAGES
    # -----------------------------------------------------

    with tab1:

        st.subheader("Manage holiday packages")

        if not st.session_state.data["packages"]:
            st.info("No packages yet.")

        for p in list(st.session_state.data["packages"]):

            status = "🟢 LIVE" if p["published"] else "⚪ DRAFT"

            with st.expander(
                f"{status} • {p['title']} • {money(p['price'])}"
            ):

                title = st.text_input(
                    "Package name",
                    p["title"],
                    key=f"title_{p['id']}"
                )

                location = st.text_input(
                    "Rhodes location",
                    p["location"],
                    key=f"location_{p['id']}"
                )

                col1, col2 = st.columns(2)

                with col1:
                    nights = st.number_input(
                        "Nights",
                        1,
                        30,
                        int(p["nights"]),
                        key=f"nights_{p['id']}"
                    )

                    airport = st.text_input(
                        "Departure airport",
                        p["departure_airport"],
                        key=f"airport_{p['id']}"
                    )

                    price = st.number_input(
                        "Total family price (£)",
                        min_value=0,
                        value=int(p["price"]),
                        step=50,
                        key=f"price_{p['id']}"
                    )

                with col2:

                    start = st.date_input(
                        "Departure date",
                        date.fromisoformat(p["start_date"]),
                        key=f"start_{p['id']}"
                    )

                    end = st.date_input(
                        "Return date",
                        date.fromisoformat(p["end_date"]),
                        key=f"end_{p['id']}"
                    )

                    spaces = st.number_input(
                        "Packages available",
                        min_value=0,
                        value=int(p["spaces"]),
                        key=f"spaces_{p['id']}"
                    )

                villa = st.text_input(
                    "Villa / accommodation",
                    p["villa"],
                    key=f"villa_edit_{p['id']}"
                )

                image = st.text_input(
                    "Main photo URL",
                    p.get("image", ""),
                    key=f"image_{p['id']}"
                )

                description = st.text_area(
                    "Description",
                    p["description"],
                    key=f"description_{p['id']}"
                )

                activities = st.text_area(
                    "Activities included",
                    p.get("activities", ""),
                    key=f"activities_{p['id']}"
                )

                support_hours = st.number_input(
                    "Child/family support hours",
                    min_value=0,
                    value=int(p.get("support_hours", 0)),
                    key=f"support_{p['id']}"
                )

                a, b, c = st.columns(3)

                with a:
                    flights = st.checkbox(
                        "Flights included",
                        p.get("flights", True),
                        key=f"flights_{p['id']}"
                    )

                with b:
                    transfers = st.checkbox(
                        "Transfers included",
                        p.get("transfers", True),
                        key=f"transfers_{p['id']}"
                    )

                with c:
                    breakfast = st.checkbox(
                        "Breakfast included",
                        p.get("breakfast", True),
                        key=f"breakfast_{p['id']}"
                    )

                published = st.checkbox(
                    "🟢 Published — customers can see this",
                    p.get("published", False),
                    key=f"published_{p['id']}"
                )

                featured = st.checkbox(
                    "✨ Featured deal",
                    p.get("featured", False),
                    key=f"featured_{p['id']}"
                )

                save_col, delete_col = st.columns(2)

                with save_col:

                    if st.button(
                        "💾 Save changes",
                        key=f"save_{p['id']}",
                        type="primary",
                        use_container_width=True
                    ):

                        p.update({
                            "title": title,
                            "location": location,
                            "nights": nights,
                            "departure_airport": airport,
                            "price": price,
                            "start_date": start.isoformat(),
                            "end_date": end.isoformat(),
                            "spaces": spaces,
                            "villa": villa,
                            "image": image,
                            "description": description,
                            "activities": activities,
                            "support_hours": support_hours,
                            "flights": flights,
                            "transfers": transfers,
                            "breakfast": breakfast,
                            "published": published,
                            "featured": featured
                        })

                        save_data(st.session_state.data)
                        st.success("Package updated ❤️")

                with delete_col:

                    if st.button(
                        "🗑 Delete package",
                        key=f"delete_{p['id']}",
                        use_container_width=True
                    ):

                        st.session_state.data["packages"] = [
                            x for x in st.session_state.data["packages"]
                            if x["id"] != p["id"]
                        ]

                        save_data(st.session_state.data)
                        st.rerun()


    # -----------------------------------------------------
    # CREATE PACKAGE
    # -----------------------------------------------------

    with tab2:

        st.subheader("Create a new Rhodes holiday")

        with st.form("new_package"):

            title = st.text_input(
                "Package name",
                placeholder="e.g. Lindos Summer Family Escape"
            )

            location = st.text_input(
                "Location",
                value="Rhodes, Greece"
            )

            c1, c2 = st.columns(2)

            with c1:

                nights = st.number_input(
                    "Nights",
                    1,
                    30,
                    7
                )

                airport = st.text_input(
                    "UK departure airport",
                    value="Manchester"
                )

                start = st.date_input(
                    "Departure date"
                )

                price = st.number_input(
                    "Total package price (£)",
                    min_value=0,
                    value=2000,
                    step=50
                )

            with c2:

                villa = st.text_input(
                    "Villa / accommodation"
                )

                end = st.date_input(
                    "Return date"
                )

                spaces = st.number_input(
                    "Number available",
                    min_value=0,
                    value=1
                )

                support_hours = st.number_input(
                    "Support hours included",
                    min_value=0,
                    value=20
                )

            image = st.text_input(
                "Main photo URL"
            )

            description = st.text_area(
                "Package description"
            )

            activities = st.text_area(
                "Activities included"
            )

            flights = st.checkbox(
                "✈️ Flights included",
                True
            )

            transfers = st.checkbox(
                "🚐 Airport transfers included",
                True
            )

            breakfast = st.checkbox(
                "🍳 Breakfast / catering included",
                True
            )

            featured = st.checkbox(
                "✨ Feature this deal"
            )

            published = st.checkbox(
                "🟢 Publish immediately"
            )

            create = st.form_submit_button(
                "➕ Create holiday package",
                type="primary",
                use_container_width=True
            )

            if create:

                if not title or not villa:
                    st.error(
                        "Add at least a package name and accommodation."
                    )

                else:

                    new_package = {
                        "id": int(datetime.now().timestamp()),
                        "title": title,
                        "location": location,
                        "nights": nights,
                        "departure_airport": airport,
                        "start_date": start.isoformat(),
                        "end_date": end.isoformat(),
                        "villa": villa,
                        "price": price,
                        "spaces": spaces,
                        "flights": flights,
                        "transfers": transfers,
                        "breakfast": breakfast,
                        "support_hours": support_hours,
                        "activities": activities,
                        "description": description,
                        "image": image,
                        "featured": featured,
                        "published": published
                    }

                    st.session_state.data["packages"].append(
                        new_package
                    )

                    save_data(st.session_state.data)

                    st.success(
                        "☀️ Package created. "
                        "If published, customers can now see it."
                    )


    # -----------------------------------------------------
    # ENQUIRIES
    # -----------------------------------------------------

    with tab3:

        st.subheader("Family enquiries")

        enquiries = st.session_state.data["enquiries"]

        if not enquiries:
            st.info("No enquiries yet.")

        for enquiry in reversed(enquiries):

            with st.expander(
                f"📩 {enquiry['name']} • "
                f"{enquiry['package']} • "
                f"{enquiry['status']}"
            ):

                st.write(f"**Email:** {enquiry['email']}")
                st.write(f"**Phone:** {enquiry['phone']}")

                st.write(
                    f"**Family:** {enquiry['adults']} adults • "
                    f"{enquiry['children']} children"
                )

                st.markdown("---")

                st.write(
                    "**Communication:**",
                    enquiry["communication"]
                )

                st.write(
                    "**Sensory preferences:**",
                    enquiry["sensory"]
                )

                st.write(
                    "**Interests:**",
                    enquiry["interests"]
                )

                st.write(
                    "**Food:**",
                    enquiry["food"]
                )

                st.write(
                    "**Routine / transitions:**",
                    enquiry["routine"]
                )

                st.write(
                    "**Requested support:**",
                    enquiry["support"]
                )

                statuses = [
                    "New",
                    "Contacted",
                    "Quote sent",
                    "Reserved",
                    "Booked",
                    "Closed"
                ]

                current = enquiry.get("status", "New")

                new_status = st.selectbox(
                    "Status",
                    statuses,
                    index=statuses.index(current)
                    if current in statuses else 0,
                    key=f"status_{enquiry['id']}"
                )

                if st.button(
                    "Save enquiry status",
                    key=f"enquiry_save_{enquiry['id']}"
                ):

                    enquiry["status"] = new_status
                    save_data(st.session_state.data)
                    st.success("Status updated.")


    # -----------------------------------------------------
    # REVIEWS
    # -----------------------------------------------------

    with tab4:

        st.subheader("Community reviews")

        reviews = st.session_state.data["reviews"]

        if not reviews:
            st.info("No reviews yet.")

        for i, review in enumerate(reviews):

            status = (
                "🟢 Published"
                if review.get("approved")
                else "🟠 Waiting approval"
            )

            with st.expander(
                f"{status} • {review['name']}"
            ):

                st.write("⭐" * int(review["rating"]))
                st.write(review["text"])

                approved = st.checkbox(
                    "Publish this review",
                    review.get("approved", False),
                    key=f"review_{i}"
                )

                if st.button(
                    "Save review",
                    key=f"review_save_{i}"
                ):

                    review["approved"] = approved
                    save_data(st.session_state.data)
                    st.success("Review updated.")

    st.markdown("---")

    if st.button("🔒 Log Nicola out"):
        st.session_state.admin_logged_in = False
        go("Home")


# =========================================================
# ROUTER
# =========================================================

page = st.session_state.page

if page == "Home":
    home_page()

elif page == "Packages":
    packages_page()

elif page == "Package":
    package_page()

elif page == "Enquiry":
    enquiry_page()

elif page == "Villas":
    villas_page()

elif page == "Community":
    community_page()

elif page == "Admin":
    admin_page()

else:
    home_page()


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")
st.caption(
    "ExploreAmore • Rhodes, Greece 🇬🇷 • "
    "Family holidays designed around individual needs."
)
st.caption(
    "*Prototype package information and pricing. "
    "Live supplier availability, payment protection and booking "
    "infrastructure must be connected before taking real bookings."
)
