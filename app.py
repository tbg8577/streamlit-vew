import pandas as pd
import streamlit as st

# view = [100, 150, 30]
# view
# st.bar_chart(view)

# public_gsheets_url = "https://docs.google.com/spreadsheets/d/1T50IexdJ9h4m7eetoo8JUfXfq1sb6mYBXFZiPUftAUQ/edit?usp=sharing"
public_gsheets_url

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

# -------------------
# @st.cache_data(ttl=600)
# def load_data(sheets_url):
#     csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
#     return pd.read_csv(csv_url)

# df = load_data(st.secrets["public_gsheets_url"])

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")
