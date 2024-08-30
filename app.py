import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pandas_gbq
import pandas 
from google.oauth2 import service_account
from google.cloud import bigquery
import statsmodels.api as sm
from plotly.subplots import make_subplots
from prophet import Prophet
from datetime import datetime, timedelta

st.set_page_config(page_title="Account Overview Dash",page_icon="🧑‍🚀",layout="wide")

def password_protection():
        main_dashboard()

def main_dashboard():
    st.markdown("<h1 style='text-align: center;'>Freedom GDN Testing</h1>", unsafe_allow_html=True)
    # Calculate the date one year ago from today
    one_year_ago = (datetime.now() - timedelta(days=365)).date()
    
    if 'full_data' not in st.session_state:
        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"]
        )
        client = bigquery.Client(credentials=credentials)
        # Modify the query
        query = f"""
        SELECT Date, Impressions, Clicks, Cost, Conversions, Campaign
        FROM `freedom_solar_segments.platform_data`
        WHERE DATE(Date) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 2 MONTH) AND DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
        AND Campaign IN ('G_S_Demand_Gen_TX_ATX/SA', 'G_S_Demand_Gen_FL', 'G_S_Demand_Gen_TX_Dallas', 'G_S_Demand_Gen_TX_Houston', 'G_S_Display_TX_Dallas', 'G_S_Display_FL', 'G_S_Display_TX_ATX/SA');"""
        st.session_state.full_data = pandas.read_gbq(query, credentials=credentials)

password_protection()

