import streamlit as st

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="IDX Investment Intelligence",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("IDX Investment Intelligence")

ticker = st.sidebar.text_input(
    "Kode Saham IDX",
    value="BBCA"
).upper()

st.sidebar.markdown("---")

st.sidebar.info(
    """
    V1 Foundation
    
    Data Source:
    - Yahoo Finance
    
    Coming Soon:
    - DCF
    - Piotroski
    - Altman Z
    - Beneish
    - CAGR Engine
    """
)

# ==========================================
# HEADER
# ==========================================

st.title("📈 IDX Investment Intelligence")

st.caption(
    "Value Investing + Growth Investing + Quality Investing + Technical Analysis"
)

# ==========================================
# TABS
# ==========================================

tabs = st.tabs([
    "Dashboard",
    "Overview",
    "Valuation",
    "Growth",
    "Quality",
    "Risk",
    "Technical",
    "Recommendation"
])

# ==========================================
# DASHBOARD
# ==========================================

with tabs[0]:

    st.subheader("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Current Price", "-")
    col2.metric("Fair Value", "-")
    col3.metric("MOS", "-")
    col4.metric("Overall Score", "-")

# ==========================================
# OVERVIEW
# ==========================================

with tabs[1]:

    st.subheader("Company Overview")

    st.info(
        f"""
        Ticker:
        {ticker}
        """
    )

# ==========================================
# VALUATION
# ==========================================

with tabs[2]:

    st.subheader("Valuation")

    st.write("DCF")
    st.write("Graham")
    st.write("Justified PBV")

# ==========================================
# GROWTH
# ==========================================

with tabs[3]:

    st.subheader("Growth")

    st.write("Revenue CAGR")
    st.write("EPS CAGR")
    st.write("BVPS CAGR")

# ==========================================
# QUALITY
# ==========================================

with tabs[4]:

    st.subheader("Quality")

    st.write("ROE")
    st.write("ROIC")
    st.write("Margins")

# ==========================================
# RISK
# ==========================================

with tabs[5]:

    st.subheader("Risk")

    st.write("Piotroski")
    st.write("Altman Z")
    st.write("Beneish")

# ==========================================
# TECHNICAL
# ==========================================

with tabs[6]:

    st.subheader("Technical")

    st.write("MA20")
    st.write("MA50")
    st.write("MA200")
    st.write("RSI")

# ==========================================
# RECOMMENDATION
# ==========================================

with tabs[7]:

    st.subheader("Final Recommendation")

    st.write("BUY / HOLD / AVOID")
