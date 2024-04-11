from openai import OpenAI
import streamlit as st
import streamlit.components.v1 as components

OpenAI.api_key = st.secrets["OPENAI_API_KEY"]

import streamlit as st

# Path to your background image
background_image_path = "images/tattooCanvas2.png"
st.image(background_image_path, use_column_width=True)

# Assuming color_options and technique_options are defined elsewhere in your code
color_options = ["B/W", "Color"]
technique_options = ["Basic", "Traditional/Old-School", "Tribal", "Japanese"]

# App Title
st.sidebar.markdown("<h2 style='color:black; font-weight:bold; font-size:43px; padding-bottom: 70px; padding-top: -70px; text-align: center;'>Tattoo?\n Yes Please!</h2>", unsafe_allow_html=True)

# Initialize session state if not already set
if 'selected_color' not in st.session_state:
    st.session_state['selected_color'] = color_options[0]
if 'selected_technique' not in st.session_state:
    st.session_state['selected_technique'] = technique_options[0]
if 'user_message' not in st.session_state:
    st.session_state['user_message'] = ''

# Start the form
with st.form(key='my_form'):
# Sidebar widgets
    st.sidebar.selectbox("Would you like your tattoo in black and white or in color?", color_options, key='selected_color')
    st.sidebar.selectbox("Choose the technique for your tattoo:", technique_options, key='selected_technique')
    st.sidebar.text_input("Describe the idea you have for your tattoo:", key='user_message')
    

# Submit button
    submitted = st.form_submit_button(label='Generate')

        # Initialize OpenAI client
    client = OpenAI()
        
        # Prepare the prompt
    tattoo_prompt = f"{st.session_state['selected_color']} and {st.session_state['selected_technique']} sketch that will be turned into a tattoo of : "
        
        # Generate the image
    response = client.images.generate(
        model="dall-e-3",
        prompt=tattoo_prompt + st.session_state['user_message'], 
        quality="hd",
        style="vivid",
        size="1024x1024",
        n=1,
    )
      # Display the background image
image_url = response.data[0].url

if image_url:
    background_image_path = image_url
    st.image(image_url, use_column_width=True)
      
       