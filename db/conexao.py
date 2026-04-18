import streamlit as st
from supabase import create_client

url = st.secrets["url"]
key = st.secrets["key"]

supabase = create_client(url, key)