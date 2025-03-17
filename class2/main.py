
import google.generativeai as genai
import PIL.Image   # (Python Imaging Library)  # pip install Pillow
from dotenv import load_dotenv  # uv add  python-dotenv 
import streamlit as st

load_dotenv()   

chat_Key= st.secrets["api"]["secrate_key"]
genai.configure(api_key = chat_Key)

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("hello my name is tehreem")

# print(response.text)

## Use images in your prompt

img = PIL.Image.open('Schoolgirls_in_Bamozai.JPG')
# img.show()
response = model.generate_content(["es image ma kiya horha hai ya kis chiz ki imag hai ya btao", img])
# print(response.text)


## Use chat history

chat = model.start_chat(history=[])
response = chat.send_message("hello my name is tehreem")
# print(response.text)

response = chat.send_message("what is my name")
# print(response.text)

# print(chat.history)

# Set the temperature

model = genai.GenerativeModel(  
    'gemini-2.0-flash',
    generation_config=genai.GenerationConfig(
        max_output_tokens=26,
        temperature=0.2,
    ) )

response = model.generate_content("how can you help me")
print(response.text)





model = genai.GenerativeModel(  
    'gemini-2.0-flash',
    generation_config=genai.GenerationConfig(
        max_output_tokens=26,
        temperature=0.9
    ) )

response = model.generate_content("how can you help me")
print(response.text)



# Stop sequences
model = genai.GenerativeModel(  'gemini-2.0-flash')

response = model.generate_content(
    'Give me a numbered list of cat facts.',
    # Limit to 5 facts.
    generation_config = genai.GenerationConfig(stop_sequences=['\n6'])
)

print(response.text)
