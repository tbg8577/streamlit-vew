import pandas as pd
import streamlit as st
import requests

# view = [100, 150, 30]
# view
# st.bar_chart(view)

st.secrets["public_gsheets_url"]

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

# -------------------
# @st.cache_data(ttl=600)
# def load_data(sheets_url):
#     csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
#     return pd.read_csv(csv_url)

# df = load_data(st.secrets["public_gsheets_url"])

# https://docs.google.com/spreadsheets/d/1lS9Y43bYYvEPlgUbi4DwFKj9yWGTeU0XUtUksNdg0qQ/edit?usp=sharing
# https://docs.google.com/spreadsheets/d/14LqxPgN1HInUXAQdRafjGjWw2_f2_5nbxi9jmWObdP4/edit?usp=sharing

YOUR_SHEET_ID='1lS9Y43bYYvEPlgUbi4DwFKj9yWGTeU0XUtUksNdg0qQ'

r = requests.get(f'https://docs.google.com/spreadsheet/ccc?key={YOUR_SHEET_ID}&output=csv')
open('dataset.csv', 'wb').write(r.content)
df = pd.read_csv('dataset.csv')
df
df.head()

name = st.text_input('이름을 입력하세요!') 

tel_num = st.text_input('전화번호 뒷자리 4자리') 

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")
