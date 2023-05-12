import pandas as pd
from PIL import Image
import streamlit as st

# Load the dataset
data = pd.read_csv('data\clean_pub_data.csv')
image = Image.open('data\pub_image.jpg')

total_pubs = len(data)
postcodes = len(data['PostCode'].unique())
local_authorities = len(data['Local_Authority'].unique())

st.title(':red[Welcome to the Pub Finder App]')
st.header(':blue[Find pubs near you based on your Location]')
st.image(image, width= 750)
st.write('### :green[Total number of pubs in the dataset:]', total_pubs)
st.write('### :green[Number of unique postcodes in the dataset:]', postcodes)
st.write('### :green[Number of unique local authorities in the dataset:]', local_authorities)
