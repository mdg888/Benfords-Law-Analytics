"""
Forensic Accounting Anomaly Detector -- Streamlit Dashboard (Phase 10).

Run with:
    streamlit run dashboard.py

Layout:
  Sidebar : file uploader, column selectors, min-amount slider, Run button
  Tab 1   : Overview       -- risk score card + signal summary chart
  Tab 2   : Benford        -- first + second digit charts (Plotly, interactive)
  Tab 3   : Anomalies      -- duplicate table + round number table
  Tab 4   : Vendor Ranking -- colour-coded risk table + CSV download
"""
import streamlit as st

# TODO 10.1 -- set page config first (must be the first st call)
# st.set_page_config(page_title="Forensic Anomaly Detector", layout="wide")

# TODO 10.2 -- sidebar: file uploader + column selectors
# uploaded = st.sidebar.file_uploader(...)

# TODO 10.3 -- cache the pipeline so widget interactions don't re-run analysis
# @st.cache_data
# def run_analysis(file_bytes, amount_col, vendor_col, date_col, min_amount):
#     ...

# TODO 10.4 -- main tabs
# tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Benford Analysis", "Anomalies", "Vendor Ranking"])

st.title("Forensic Accounting Anomaly Detector")
st.info("Dashboard not yet implemented. Work through Phases 1-9 first, then build this.")
