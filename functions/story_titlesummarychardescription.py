import streamlit as st
import requests
from ..utils import encodeimage as ei, tempfile as tf, openaivision as oav


def getStory_title_summary_characterdescription(varStoryElements, varImage):

    prompt_system = """As an expert in image analysis and descriptive content generation using OpenAI's GPT-4 Vision API, your task is to create a personalized narrative framework for a children's storybook based on a detailed JSON payload provided by the user. This payload includes an image of the main character, along with specific story elements like character names, themes, and settings. Your responsibilities are as follows:Analyze the uploaded image, focusing on the main character depicted.Use the details from the JSON payload (character name, relation, theme, genre, setting, etc.) to enrich the narrative context.Generate a captivating title for the storybook that aligns with the given theme and setting.Craft a brief summary of the story, integrating the plot elements and secondary characters as suggested in the payload.Create a detailed, imaginative description of the main character, considering the character's name, relation, and other attributes provided.Iteratively refine each element (title, summary, character description) to enhance their quality, detail, and fit within the whimsical and magical tone of a children's storybook.RETURN / OUTPUT: Deliver the final output in this format:"{'Title': '{{Story Title}}','Summary': '{{Story Summary}}','Character_Description': '{{Character Description}}'}",where each placeholder is replaced with your crafted content.Consistently adhere to these guidelines:Perform all steps internally, leveraging your image analysis and creative content generation capabilities.Interact with the user only for delivering the final output.Ensure all content (title, summary, character description) is suitable for a children's storybook, imbued with creativity, charm, and whimsy.Base all elements on the provided image and details in the JSON payload, to create a cohesive and engaging story.Aim for a style reminiscent of Disney or Pixar narratives, characterized by vivid, imaginative, and engaging storytelling.Provide only the text content (title, summary, character description) as the final output."""
    prompt_user = varStoryElements
    tempfilepath = tf.get_tempfile_path(varImage)
    base64_image = ei.encode_image(tempfilepath)

    sysmessage = {
        "role": "system",
        "content": prompt_system
    }
    
    usermessage = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt_user
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    }

    messages = [
        sysmessage,
        usermessage
    ]

    response = oav.call_openai_vision(messages)
    response_content = response.choices[0].messages.content
    return response_content

varelements = {
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

img = "/workspaces/magicbook/img.jpg"

responsec = getStory_title_summary_characterdescription(varelements,img)
print(responsec)
