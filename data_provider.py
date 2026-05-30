import yfinance as yf
import pandas as pd
import streamlit as st


# ==========================================
# HELPERS
# ==========================================

def format_ticker(ticker: str) -> str:
    """
    Convert BBCA -> BBCA.JK
    """

    ticker = ticker.upper().strip()

    if not ticker.endswith(".JK"):
        ticker += ".JK"

    return ticker


# ==========================================
# MAIN DATA LOADER
# ==========================================

@st.cache_data(ttl=3600)
def load_stock(ticker: str):

    symbol = format_ticker(ticker)

    stock = yf.Ticker(symbol)

    return stock


# ==========================================
# COMPANY INFO
# ==========================================

@st.cache_data(ttl=3600)
def get_company_info(ticker: str):

    try:

        stock = load_stock(ticker)

        return stock.info

    except Exception as e:

        print(e)

        return {}


# ==========================================
# PRICE HISTORY
# ==========================================

@st.cache_data(ttl=3600)
def get_price_history(
    ticker: str,
    period: str = "10y"
):

    try:

        stock = load_stock(ticker)

        df = stock.history(
            period=period,
            auto_adjust=True
        )

        return df

    except Exception as e:

        print(e)

        return pd.DataFrame()


# ==========================================
# INCOME STATEMENT
# ==========================================

@st.cache_data(ttl=3600)
def get_income_statement(ticker: str):

    try:

        stock = load_stock(ticker)

        return stock.financials

    except Exception as e:

        print(e)

        return pd.DataFrame()


# ==========================================
# BALANCE SHEET
# ==========================================

@st.cache_data(ttl=3600)
def get_balance_sheet(ticker: str):

    try:

        stock = load_stock(ticker)

        return stock.balance_sheet

    except Exception as e:

        print(e)

        return pd.DataFrame()


# ==========================================
# CASH FLOW
# ==========================================

@st.cache_data(ttl=3600)
def get_cashflow(ticker: str):

    try:

        stock = load_stock(ticker)

        return stock.cashflow

    except Exception as e:

        print(e)

        return pd.DataFrame()


# ==========================================
# DIVIDEND HISTORY
# ==========================================

@st.cache_data(ttl=3600)
def get_dividends(ticker: str):

    try:

        stock = load_stock(ticker)

        return stock.dividends

    except Exception as e:

        print(e)

        return pd.Series(dtype=float)


# ==========================================
# SHARES OUTSTANDING
# ==========================================

@st.cache_data(ttl=3600)
def get_shares_outstanding(ticker: str):

    try:

        info = get_company_info(ticker)

        return info.get(
            "sharesOutstanding",
            None
        )

    except:

        return None


# ==========================================
# MARKET CAP
# ==========================================

@st.cache_data(ttl=3600)
def get_market_cap(ticker: str):

    try:

        info = get_company_info(ticker)

        return info.get(
            "marketCap",
            None
        )

    except:

        return None


# ==========================================
# CURRENT PRICE
# ==========================================

@st.cache_data(ttl=300)
def get_current_price(ticker: str):

    try:

        df = get_price_history(
            ticker,
            period="5d"
        )

        return float(
            df["Close"].iloc[-1]
        )

    except:

        return None


# ==========================================
# MASTER FUNCTION
# ==========================================

@st.cache_data(ttl=3600)
def get_company_data(ticker: str):

    return {

        "info":
            get_company_info(ticker),

        "price":
            get_current_price(ticker),

        "market_cap":
            get_market_cap(ticker),

        "shares":
            get_shares_outstanding(ticker),

        "income_statement":
            get_income_statement(ticker),

        "balance_sheet":
            get_balance_sheet(ticker),

        "cashflow":
            get_cashflow(ticker),

        "history":
            get_price_history(ticker),

        "dividends":
            get_dividends(ticker)
    }
