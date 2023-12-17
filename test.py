import requests
import streamlit as st
import base64


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

path = encode_image("/workspaces/magicbook/img.jpg")


url = st.secrets.powerautomate.pavision
payload = {
  "uploaded_image_data": path,
  "uploaded_image_urlpath": "path/to/uploaded_image.png",
  "character_name": "John Doe",
  "relation_to_character": "Father",
  "theme_description": "Adventure",
  "theme_category": "Adventure",
  "genre": "Fantasy",
  "setting": "Enchanted Forest",
  "plot_element": "Treasure Hunt",
  "secondary_character": "Talking Animal",
  "magical_object": "Magic Wand"
}

response = requests.post(url=url, json=payload)

print(response)